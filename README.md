<div align="center">

# 🟢 Matrix Chat Python

### Real-Time Flask + Socket.IO Web Chat with Matrix-Inspired UI

**Python • Flask • Flask-SocketIO • HTML • CSS • JavaScript**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask&logoColor=white)
![Socket.IO](https://img.shields.io/badge/Realtime-Socket.IO-010101?logo=socketdotio&logoColor=white)
![UI](https://img.shields.io/badge/Style-Matrix-00ff66)

</div>

---

## 🚀 About

**Matrix Chat Python** is a lightweight real-time web chat experiment built with Flask and Flask-SocketIO. The frontend uses HTML, CSS and JavaScript with a visual style inspired by Matrix terminals.

Connected clients can exchange messages instantly, while new connections receive the current in-memory message history. The project is intentionally compact and easy to understand, making it useful as a starting point for learning real-time Python web communication.

It is designed for users searching for a **Flask Socket.IO chat**, **Python real-time chat**, **Matrix style chat**, **Flask web chat source code** or a simple Socket.IO messaging example.

---

## ✨ Features

| Feature | Description |
|---|---|
| ⚡ Real-time messaging | Socket.IO communication between clients and server |
| 🐍 Flask backend | Lightweight Python web server |
| 🟢 Matrix UI | Terminal-inspired green visual style |
| 📣 Broadcast | Messages are sent to connected clients |
| 🧠 Message history | New clients receive history stored in server memory |
| 🪶 Small project | Simple structure for learning and modification |

---

## 📦 Installation

```bash
git clone https://github.com/Swir/Matrix-czat-pythom.git
cd Matrix-czat-pythom
pip install flask flask-socketio
python server.py
```

Then open the local server URL in your browser.

---

## 🧠 Architecture

```text
Browser A ─┐
           ├── Socket.IO ──► Flask Server ──► In-memory history
Browser B ─┘
```

---

## ⚠️ Development Status

The current server starts in development/debug mode and stores message history only in RAM. Restarting the process clears that history. Treat this repository as an experimental/development project rather than a production messaging service.

For public deployment, review authentication, persistence, HTTPS, rate limiting, input handling and production server configuration.

---

## 🔍 Discoverability

`flask socketio chat` • `python realtime chat` • `matrix chat python` • `flask web chat` • `socket.io python example` • `realtime messaging flask` • `matrix style web chat` • `python chat source code`

---

## 👨‍💻 Author

Developed by **Swir** — [@Swir](https://github.com/Swir)

<div align="center">

### 🟢 Flask + Socket.IO + Matrix vibes

⭐ **Star the repository if you like the project!**

</div>
