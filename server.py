from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Historia wiadomości
message_history = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    sid = request.sid  # można pominąć, bo sid jest już dostępne jako argument funkcji
    print(f'Użytkownik {sid} dołączył do czatu.')
    # Wysłanie historii wiadomości do nowo podłączonego użytkownika
    emit('message_history', message_history, room=sid)

@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    print(f'Użytkownik {sid} opuścił czat.')

@socketio.on('message')
def handle_message(data):
    sid = request.sid
    print(f'Wiadomość od {sid}: {data}')
    # Dodawanie wiadomości do historii
    message_history.append({'sid': sid, 'message': data})
    # Wysyłanie wiadomości do wszystkich podłączonych użytkowników
    emit('message', {'sid': sid, 'message': data}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
