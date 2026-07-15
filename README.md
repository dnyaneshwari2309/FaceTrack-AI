# 🚀 FaceTrack AI

## 🎯 Smart Face Recognition Attendance Management System

FaceTrack AI is an **AI-powered attendance management system** that uses **Face Recognition Technology** to automatically identify students and mark attendance.  

Built using **Python, Flask, and OpenCV**, this system provides a simple and efficient way to manage attendance through a modern web interface.

---

# ✨ Features

✅ **Student Enrollment**  
🖥️ Register student details into the system  

📷 **Face Capture using Webcam**  
Capture student face images for training  

👁️ **Face Detection using Haar Cascade**  
Detect faces accurately from webcam input  

🤖 **Face Recognition using LBPH Algorithm**  
Recognize registered students in real-time  

📝 **Automated Attendance Marking**  
Automatically record attendance after successful recognition  

📊 **Attendance Reports**  
View and manage attendance records  

🌐 **Modern Dashboard UI**  
Easy-to-use web interface for attendance management  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core Programming Language |
| 🌐 Flask | Web Application Framework |
| 👁️ OpenCV | Computer Vision & Face Recognition |
| 🧠 LBPH Algorithm | Face Recognition Model |
| 🔢 NumPy | Numerical Computation |
| 🎨 HTML/CSS | Frontend Design |
| 📄 CSV | Attendance Data Storage |

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
├── screenshots/
│   ├── dashboard.png
│   ├── register.png
│   └── attendance.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dnyaneshwari2309/FaceTrack-AI.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd FaceTrack-AI
```

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask opencv-contrib-python numpy
```

### 4️⃣ Run the Application

```bash
python "Face Recognition Attendance System.py"
```

🎉 The application will start running on your local server.

---

# 🔄 How It Works

1️⃣ 👤 Register student details  
2️⃣ 📷 Capture face images using webcam  
3️⃣ 🧠 Train the face recognition model  
4️⃣ 🔍 Start real-time face recognition  
5️⃣ ✅ Attendance is automatically marked  
6️⃣ 📊 View attendance reports from the dashboard  

---

# 📸 Screenshots

### 🏠 Dashboard

![Dashboard](screenshots/dashboard.png)

### 👤 Student Registration

![Registration](screenshots/register.png)

### 📊 Attendance Report

![Attendance](screenshots/attendance.png)

---

# 📦 Requirements

```
Flask
opencv-contrib-python
numpy
```

---

# 🚫 .gitignore

```
__pycache__/
*.pyc
venv/
trainer/
Attendance/
dataset/
```

The following files are excluded:

❌ Training data  
❌ Generated face recognition models  
❌ Attendance records  
❌ Virtual environment files  

---

# 🚀 Future Enhancements

🔹 MySQL Database Integration  
🔹 Cloud Deployment  
🔹 Real-Time Attendance Notifications  
🔹 Multiple Camera Support  
🔹 Deep Learning Based Face Recognition  
🔹 Mobile Application Integration  

---

# 👩‍💻 Author

**Dnyaneshwari Sonawane**

🎓 B.E. Artificial Intelligence & Data Science  

