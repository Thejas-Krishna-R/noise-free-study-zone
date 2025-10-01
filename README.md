# 🎧 Noise-Free Study Zone

A professional web application that helps you focus better by analyzing background noise and playing appropriate white noise in a loop during study sessions.

![App Preview](https://via.placeholder.com/800x400/667eea/ffffff?text=Noise-Free+Study+Zone)

## ✨ Features

### 🎯 Core Functionality
- **Smart Noise Analysis** - Analyzes background noise in 3 seconds
- **Random White Noise** - Plays 1 of 7 different white noise files
- **Session Management** - Start, pause, resume, and stop sessions
- **Task Tracking** - Enter task names and track focus time
- **Pause Duration Tracking** - Monitors how long you were paused

### 📊 Advanced Dashboard
- **Statistics Overview** - Total time, sessions, averages
- **Daily Charts** - Visual progress tracking with Recharts
- **Session History** - Complete record of all sessions
- **Beautiful Graphs** - Professional data visualization

### 🎨 Professional Design
- **Purple/Blue Theme** - Modern, calming color palette
- **Responsive Layout** - Works on desktop and mobile
- **Smooth Animations** - Professional user experience
- **Clean Interface** - Easy to use and understand

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher)
- Python 3.7+ (for AI server)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Thejas-Krishna-R/noise-free-study-zone.git
   cd noise-free-study-zone
   ```

2. **Install React dependencies**
   ```bash
   cd client
   npm install --legacy-peer-deps
   ```

3. **Install Python dependencies (for AI server)**
   ```bash
   cd ../ai_server
   pip install flask flask-cors librosa numpy
   ```

4. **Start the application**
   
   **Terminal 1 - React App:**
   ```bash
   cd client
   npm start
   ```
   
   **Terminal 2 - AI Server (optional):**
   ```bash
   cd ai_server
   python ai_server.py
   ```

5. **Open your browser**
   - Navigate to `http://localhost:3000`
   - The app will work with or without the AI server (fallback included)

## 🎵 How to Use

1. **Enter a task name** (e.g., "Studying Math", "Coding", "Reading")
2. **Click "Start Focus Session"**
3. **Wait 3 seconds** for background noise analysis
4. **White noise starts playing automatically** in a loop
5. **Use pause/resume** as needed during your session
6. **Click "Stop Session"** when finished
7. **View your progress** in the dashboard

## 🛠️ Tech Stack

### Frontend
- **React 18** - Modern UI framework
- **Recharts** - Beautiful data visualization
- **Lucide React** - Professional icons
- **CSS3** - Custom styling with gradients and animations

### Backend
- **Flask** - Python web framework for AI server
- **Librosa** - Audio analysis and processing
- **NumPy** - Numerical computing

### Features
- **Web Audio API** - Real-time audio processing
- **MediaRecorder API** - Audio recording
- **Canvas API** - Waveform visualization
- **Local Storage** - Session data persistence

## 📁 Project Structure

```
noise-free-study-zone/
├── client/                 # React frontend
│   ├── public/
│   │   └── noises/        # White noise audio files
│   ├── src/
│   │   ├── App.js         # Main application component
│   │   ├── App.css        # Styling
│   │   └── index.js       # React entry point
│   └── package.json
├── ai_server/             # Python AI server
│   └── ai_server.py       # Noise analysis server
├── server/                # Express server (optional)
│   └── index.js
└── README.md
```

## 🎨 Screenshots

### Main Interface
- Clean, professional design
- Task input and session controls
- Real-time session status

### Dashboard
- Statistics overview
- Daily focus time charts
- Session history

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Thejas Krishna R**
- GitHub: [@Thejas-Krishna-R](https://github.com/Thejas-Krishna-R)

## 🙏 Acknowledgments

- White noise files for focus enhancement
- React community for excellent documentation
- Recharts for beautiful data visualization
- Lucide for professional icons

---

**Happy Focusing! 🎧✨**

