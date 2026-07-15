# 🚀 FaceTrack AI

## 🎯 Smart Face Recognition Attendance Management System

FaceTrack AI is an **AI-powered attendance management system** that automates the traditional attendance process using **Face Recognition Technology**.

The system uses **Computer Vision and Machine Learning techniques** to detect and recognize students through a webcam and automatically record their attendance. It is developed using **Python, Flask, and OpenCV** with an interactive web-based interface.

The main goal of this project is to reduce manual attendance efforts, improve accuracy, and provide a faster and smarter attendance management solution.

---

# 🌟 Key Features

👨‍🎓 **Student Enrollment**
- Add and manage student information.
- Assign unique IDs for each registered student.

📷 **Face Image Capture**
- Capture multiple face samples using a webcam.
- Generate a dataset for model training.

👁️ **Real-Time Face Detection**
- Detect faces using Haar Cascade Classifier.
- Works with live webcam input.

🤖 **Face Recognition System**
- Recognizes registered students using the LBPH (Local Binary Pattern Histogram) algorithm.
- Provides real-time identification.

📝 **Automatic Attendance Marking**
- Marks attendance automatically after successful face recognition.
- Avoids manual attendance errors.

📊 **Attendance Management**
- Stores attendance records.
- Allows easy access to attendance reports.

🌐 **Web-Based Dashboard**
- User-friendly interface built using Flask.
- Provides smooth navigation between modules.

---

# 🎯 Project Objectives

The main objectives of FaceTrack AI are:

✅ Automate the attendance management process  
✅ Reduce paperwork and manual efforts  
✅ Improve attendance accuracy  
✅ Provide real-time face recognition  
✅ Maintain organized attendance records  
✅ Demonstrate practical applications of AI and Computer Vision  

---

# 🧠 How FaceTrack AI Works

The system follows a simple AI-based workflow:

### 1️⃣ Student Registration
- Student details are entered into the system.
- A unique identification number is assigned.

### 2️⃣ Face Data Collection
- Webcam captures multiple images of the student's face.
- Images are stored for training.

### 3️⃣ Model Training
- Collected face images are processed.
- LBPH algorithm creates a face recognition model.

### 4️⃣ Face Recognition
- Live webcam feed captures faces.
- The trained model compares the detected face with stored data.

### 5️⃣ Attendance Generation
- If a match is found, attendance is automatically recorded.
- Attendance details are stored for future reference.

---

# 🛠️ Technologies Used

| Technology | Description |
|------------|-------------|
| 🐍 Python | Core programming language |
| 🌐 Flask | Backend web framework |
| 👁️ OpenCV | Computer vision operations |
| 🧠 LBPH Algorithm | Face recognition technique |
| 🔢 NumPy | Numerical processing |
| 🎨 HTML/CSS | User interface development |
| 📄 CSV | Attendance data storage |

---

# 📂 Project Structure

```text
FaceTrack-AI/
│
├── Face Recognition Attendance System.py
├── haarcascade_frontalface_default.xml
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── train.html
│   ├── attendance.html
│   └── view_attendance.html
│
├── static/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/dnyaneshwari2309/FaceTrack-AI.git
```

## 2️⃣ Open Project Directory

```bash
cd FaceTrack-AI
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

or manually install:

```bash
pip install flask opencv-contrib-python numpy
```

## 4️⃣ Run the Application

```bash
python "Face Recognition Attendance System.py"
```

The application will start successfully on your local system.

---

# 📦 Requirements

```
Flask
opencv-contrib-python
numpy
```

---

# 🔐 Data Privacy & File Management

The following files are excluded from GitHub using `.gitignore`:

```
__pycache__/
*.pyc
venv/
trainer/
Attendance/
dataset/
```

These include:

❌ Face training datasets  
❌ Generated recognition models  
❌ Attendance records  
❌ Virtual environment files  

---

# 💡 Applications

FaceTrack AI can be used in:

🏫 Educational Institutions  
🏢 Corporate Offices  
🏭 Industrial Workplaces  
🏥 Healthcare Organizations  
🎓 Training Centers  

---

# 🚀 Future Enhancements

🔹 Integration with MySQL/PostgreSQL database  
🔹 Cloud-based attendance storage  
🔹 Deep Learning based face recognition using CNN models  
🔹 Multiple camera support  
🔹 Email/SMS attendance notifications  
🔹 Admin authentication system  
🔹 Mobile application integration  
🔹 Attendance analytics dashboard  

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

✅ Computer Vision using OpenCV  
✅ Face Detection and Recognition  
✅ Flask Web Development  
✅ Machine Learning Algorithms  
✅ Data Handling and Processing  
✅ Building AI-based real-world applications  

---

# 👩‍💻 Author

**Dnyaneshwari Sonawane**

🎓 B.E. Artificial Intelligence & Data Science

