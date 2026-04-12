🚀 FixMyCity ChatBot

An intelligent chatbot system built as part of the FixMyCity project that assists users in reporting civic issues like potholes, garbage, and electrical faults. The chatbot interacts with users, collects complaint details, and integrates with an AI model for automated issue classification.

📌 Overview

FixMyCity ChatBot is designed to:

🧠 Understand user complaints via chat interface
📸 Accept image inputs for issue detection
🤖 Use AI (MobileNetV2) to classify issues
📍 Help users report problems efficiently
⚡ Provide fast and structured complaint submission
🧠 Features
💬 Interactive chatbot interface
🖼️ Image-based issue classification (AI-powered)
📂 Supports categories:
Potholes
Garbage
Electrical faults
🔗 FastAPI backend integration
⚙️ Lightweight and efficient (optimized for CPU systems)
🏗️ Tech Stack
Backend: Python, FastAPI
AI Model: TensorFlow / Keras (MobileNetV2 - Transfer Learning)
Image Processing: Pillow (PIL), OpenCV
Frontend: HTML, CSS, JavaScript (optional chatbot UI)
Environment: Python Virtual Environment (.venv)
📁 Project Structure
FixMyCity-ChatBot/
│
├── model/
│   ├── trained_model.h5
│
├── dataset/
│   ├── pothole/
│   ├── garbage/
│   ├── electrical/
│
├── api/
│   ├── main.py          # FastAPI server
│
├── chatbot/
│   ├── bot_logic.py     # Chat handling logic
│
├── static/              # Frontend files (if any)
│
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/ChatBot.git
cd ChatBot
2️⃣ Create virtual environment
python -m venv .venv

Activate it:

.venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run FastAPI server
uvicorn api.main:app --reload
5️⃣ Open in browser
http://127.0.0.1:8000/docs
🤖 How It Works
User interacts with chatbot
User uploads an image or describes issue
Image is sent to FastAPI backend
AI model classifies issue into:
Pothole
Garbage
Electrical
System logs complaint and returns response
📊 AI Model Details
Model: MobileNetV2 (Transfer Learning)
Dataset:
Pothole (~90 images)
Garbage (~76 images)
Electrical (~46 images)
Techniques:
Image augmentation
Resizing & normalization
Frozen base layers
🚧 Future Improvements
📱 Mobile app integration
📍 GPS-based complaint tagging
🗺️ Dashboard for authorities
🔔 Real-time status tracking
🧾 Complaint priority system (FixPriority integration)
🤝 Contribution

Feel free to fork the repository and contribute:

git fork
git checkout -b feature-name
📜 License

This project is for educational and academic purposes.

👨‍💻 Author

Dikshit Garg
FixMyCity Project Developer

⭐ Final Note

This chatbot is part of a larger vision to digitize and optimize civic issue reporting using AI and automation.
