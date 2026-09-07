<div align="center">

# 🟢 Matrix Chat Python

**Real-time Matrix-inspired web chat experiment by Swir**  
**Eksperymentalny czat WWW czasu rzeczywistego w stylu Matrix autorstwa Swir**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask)
![Socket.IO](https://img.shields.io/badge/Realtime-Socket.IO-010101?logo=socketdotio)
![Author](https://img.shields.io/badge/Author-Swir-00ff66)

</div>

---

## 🇬🇧 English

Matrix Chat Python is a small real-time web-chat experiment using Flask and Flask-SocketIO on the backend with HTML, CSS and JavaScript on the client side. Connected clients can exchange messages immediately and new connections receive the in-memory message history.

### ✨ Features
- real-time Socket.IO communication
- Flask backend
- Matrix-inspired frontend styling
- broadcast messages to connected users
- in-memory message history for new clients
- lightweight project structure

### 🚀 Installation

```bash
git clone https://github.com/Swir/Matrix-czat-pythom.git
cd Matrix-czat-pythom
pip install flask flask-socketio
python server.py
```

---

## 🇵🇱 Polski

Matrix Chat Python to niewielki eksperymentalny czat WWW działający w czasie rzeczywistym. Backend wykorzystuje Flask i Flask-SocketIO, a frontend HTML, CSS i JavaScript. Wiadomości są rozsyłane do podłączonych klientów, a nowy użytkownik otrzymuje historię przechowywaną w pamięci serwera.

### ✨ Funkcje
- komunikacja czasu rzeczywistego przez Socket.IO
- backend Flask
- wygląd inspirowany Matrixem
- rozsyłanie wiadomości do podłączonych użytkowników
- historia wiadomości w pamięci procesu
- prosta struktura projektu

### 🚀 Instalacja

```bash
pip install flask flask-socketio
python server.py
```

## ⚠️ Development note / Uwaga
The current server starts in debug mode and keeps history only in RAM. Treat it as a development/experimental project rather than a production chat server.

Aktualny serwer uruchamia tryb debug i przechowuje historię tylko w RAM. Projekt należy traktować jako wersję eksperymentalną/deweloperską, a nie gotowy serwer produkcyjny.

## 👤 Author / Autor
Developed by **Swir**.
