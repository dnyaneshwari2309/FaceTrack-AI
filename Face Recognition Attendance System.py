"""
Face Recognition Attendance System
-----------------------------------
A Flask web application that uses OpenCV (Haar Cascade + LBPH) to register
students' faces via webcam, train a recognition model, and automatically
mark attendance in CSV files when a registered face is detected.
"""

import cv2
import os
import csv
import pickle
import numpy as np
from datetime import datetime
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Paths & setup
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')
TRAINER_DIR = os.path.join(BASE_DIR, 'trainer')
ATTENDANCE_DIR = os.path.join(BASE_DIR, 'Attendance')
TRAINER_FILE = os.path.join(TRAINER_DIR, 'trainer.yml')
LABELS_FILE = os.path.join(TRAINER_DIR, 'labels.pickle')
CASCADE_PATH = os.path.join(BASE_DIR, "haarcascade_frontalface_default.xml")

for d in (DATASET_DIR, TRAINER_DIR, ATTENDANCE_DIR):
    os.makedirs(d, exist_ok=True)

face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

# ---------------------------------------------------------------------------
# Global (in-memory) state
# ---------------------------------------------------------------------------
camera = None
register_info = {'id': None, 'name': None, 'count': 0, 'target': 50}
recognizer = None
labels = {}
marked_today = set()


def get_camera():
    """Lazily open the default webcam."""
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0)
    return camera


def release_camera():
    global camera
    if camera is not None:
        camera.release()
        camera = None


def load_recognizer():
    """Load a previously trained LBPH model + label mapping, if present."""
    global recognizer, labels
    if os.path.exists(TRAINER_FILE) and os.path.exists(LABELS_FILE):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(TRAINER_FILE)
        with open(LABELS_FILE, 'rb') as f:
            labels = pickle.load(f)
        return True
    return False


load_recognizer()


# ---------------------------------------------------------------------------
# Video generators
# ---------------------------------------------------------------------------
def gen_register_frames():
    """Stream webcam frames while saving cropped face images for a new student."""
    global register_info
    cam = get_camera()
    folder_name = f"{register_info['id']}_{register_info['name']}"
    student_dir = os.path.join(DATASET_DIR, folder_name)
    os.makedirs(student_dir, exist_ok=True)

    while True:
        success, frame = cam.read()
        if not success:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            if register_info['count'] < register_info['target']:
                register_info['count'] += 1
                face_img = gray[y:y + h, x:x + w]
                img_path = os.path.join(student_dir, f"{register_info['count']}.jpg")
                cv2.imwrite(img_path, face_img)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"{register_info['count']}/{register_info['target']}",
                        (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

        if register_info['count'] >= register_info['target']:
            break

    release_camera()


def mark_attendance(student_id, name):
    """Append a row to today's attendance CSV (once per student per day)."""
    today = datetime.now().strftime('%Y-%m-%d')
    csv_path = os.path.join(ATTENDANCE_DIR, f"Attendance_{today}.csv")
    key = f"{student_id}_{today}"
    if key in marked_today:
        return
    file_exists = os.path.exists(csv_path)
    with open(csv_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['ID', 'Name', 'Time'])
        writer.writerow([student_id, name, datetime.now().strftime('%H:%M:%S')])
    marked_today.add(key)


def gen_attendance_frames():
    """Stream webcam frames, recognize faces, and mark attendance live."""
    cam = get_camera()
    while True:
        success, frame = cam.read()
        if not success:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_img = gray[y:y + h, x:x + w]
            display_name = "Unknown"
            color = (0, 0, 255)

            if recognizer is not None:
                label_id, confidence = recognizer.predict(face_img)
                if confidence < 70:  # lower = more confident match
                    info = labels.get(label_id)
                    if info:
                        student_id, name = info
                        display_name = name
                        color = (0, 255, 0)
                        mark_attendance(student_id, name)

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, display_name, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route('/')
def index():
    trained = os.path.exists(TRAINER_FILE)
    students = len([d for d in os.listdir(DATASET_DIR)
                    if os.path.isdir(os.path.join(DATASET_DIR, d))])
    return render_template('index.html', trained=trained, students=students)


@app.route('/register', methods=['GET', 'POST'])
def register():
    global register_info
    if request.method == 'POST':
        student_id = request.form['student_id'].strip()
        name = request.form['name'].strip()
        register_info = {'id': student_id, 'name': name, 'count': 0, 'target': 50}
        return render_template('register.html', started=True, name=name, student_id=student_id)
    return render_template('register.html', started=False)


@app.route('/video_feed_register')
def video_feed_register():
    return Response(gen_register_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/register_status')
def register_status():
    return jsonify({'count': register_info['count'], 'target': register_info['target']})


@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        faces, ids, id_labels = [], [], {}
        current_label = 0

        for student_folder in sorted(os.listdir(DATASET_DIR)):
            folder_path = os.path.join(DATASET_DIR, student_folder)
            if not os.path.isdir(folder_path):
                continue
            if '_' not in student_folder:
                continue
            student_id, name = student_folder.split('_', 1)

            for img_name in os.listdir(folder_path):
                img_path = os.path.join(folder_path, img_name)
                gray_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if gray_img is None:
                    continue
                faces.append(gray_img)
                ids.append(current_label)

            id_labels[current_label] = (student_id, name)
            current_label += 1

        if not faces:
            return render_template('train.html', done=False,
                                    error="No training data found. Please register students first.")

        recognizer_new = cv2.face.LBPHFaceRecognizer_create()
        recognizer_new.train(faces, np.array(ids))
        recognizer_new.write(TRAINER_FILE)
        with open(LABELS_FILE, 'wb') as f:
            pickle.dump(id_labels, f)

        load_recognizer()
        return render_template('train.html', done=True, count=len(faces), students=len(id_labels))

    return render_template('train.html', done=None)


@app.route('/attendance')
def attendance():
    return render_template(
        'attendance.html',
        model_ready=(recognizer is not None)
    )


@app.route('/video_feed_attendance')
def video_feed_attendance():
    return Response(gen_attendance_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stop_camera')
def stop_camera():
    release_camera()
    return jsonify({'status': 'stopped'})


@app.route('/view_attendance')
def view_attendance():
    date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
    csv_path = os.path.join(ATTENDANCE_DIR, f"Attendance_{date}.csv")
    records = []
    if os.path.exists(csv_path):
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            records = list(reader)
    return render_template('view_attendance.html', records=records, date=date)

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
