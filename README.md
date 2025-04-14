# 🚗 Vehicle Detection, Classification, and Counting 🚗

This project provides a comprehensive solution for **Vehicle Detection**, **Vehicle Classification**, and **Counting** using computer vision techniques. It utilizes various algorithms, including background subtraction, image processing, and object detection, to detect vehicles in video streams.

---

## 📦 Tech Stack & Libraries 🛠️

- **Frontend**:  
  - HTML
  - CSS
  - JavaScript (React.js)
  - Axios (for API calls)
  - Socket.io (for real-time communication)

- **Backend**:  
  - Python
  - Flask (Web framework)
  - OpenCV (Image and video processing)
  - NumPy (Mathematical operations)
  - TensorFlow/Keras (for AI models, if applicable)

- **Other Tools**:  
  - FFmpeg (for video processing)
  - Flask-SocketIO (real-time communication)

---

## 📋 Features

- 🚙 **Vehicle Detection**: Detects moving vehicles in real-time from video streams.
- 📊 **Vehicle Classification**: Classifies detected vehicles into various types (e.g., cars, trucks, motorcycles).
- 🔢 **Vehicle Counting**: Counts the number of vehicles entering or exiting a region of interest.
- 🎥 **Video Processing**: Convert, compress, and manipulate video files using FFmpeg.
- 💬 **Real-time Communication**: Frontend and backend communicate via Socket.io for a seamless experience.
- 🌍 **Cross-browser support**: Works seamlessly in modern web browsers.

---

## 🚀 How to Use

### Run this command for frontend first
npm install axios@^1.8.4 boxicons@^2.1.4 chart.js@^4.4.8 leaflet@^1.9.4 leaflet-geosearch@^4.2.0 react@^19.0.0 react-chartjs-2@^5.3.0 react-dom@^19.0.0 react-leaflet@^5.0.0 react-router-dom@^7.5.0 socket.io-client@^4.8.1 swiper@^11.2.6

### 1. Clone the Repository

```bash
git clone https://github.com/pranayvips/vehicle.git
2. Install Dependencies
Backend (Flask):
bash
Copy
Edit
# Navigate to the backend folder
cd backend

# Install required Python libraries
pip install -r requirements.txt
Frontend (React):
bash
Copy
Edit
# Navigate to the frontend folder
cd frontend

# Install required npm packages
npm install
3. Run the Backend
bash
Copy
Edit
# From the backend directory, start the Flask app
python app.py
This will run the backend server, typically on http://localhost:5000.

4. Run the Frontend
bash
Copy
Edit
# From the frontend directory, start the React development server
npm start
This will run the frontend server on http://localhost:5173.

5. Upload a Video or Stream
Once the frontend and backend are running, you can upload a video file through the frontend interface. The system will process the video, detect vehicles, classify them, and count them in real-time.

🛠️ Running Commands for Video Processing
Here are a few essential commands to process and manipulate video files:

Convert a Video:
Convert input_video.avi to output_video.mp4.

bash
Copy
Edit
ffmpeg -i input_video.avi -vcodec libx264 -acodec aac output_video.mp4
Resize Video:
Resize the video to 640x480 resolution.

bash
Copy
Edit
ffmpeg -i input_video.mp4 -vf scale=640:480 output_resized.mp4
Extract Audio:
Extract audio from the video.

bash
Copy
Edit
ffmpeg -i input_video.mp4 -q:a 0 -map a output_audio.mp3
📑 Contributing
We welcome contributions! If you'd like to contribute to this project, follow these steps:

Fork the repository

Clone your forked repository

Create a new branch for your feature or bug fix

Commit your changes

Push your changes to your fork

Open a pull request

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
For any queries or issues, feel free to reach out:

Email: your-email@example.com

GitHub: yourusername

