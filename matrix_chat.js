document.addEventListener('DOMContentLoaded', function() {
    const socket = io('http://localhost:5000');
    const messageInput = document.getElementById('messageInput');
    const messagesList = document.getElementById('messages');

    socket.on('connect', () => {
        console.log('Połączono z serwerem');
    });

    socket.on('disconnect', () => {
        console.log('Rozłączono z serwerem');
    });

    socket.on('message_history', (history) => {
        history.forEach((entry) => {
            addMessage(entry);
        });
    });

    socket.on('message', (data) => {
        addMessage(data);
    });

    document.getElementById('messageInput').addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = messageInput.value.trim();

        if (message !== '') {
            socket.emit('message', message);
            messageInput.value = '';
        }
    }

    function addMessage(data) {
        const li = document.createElement('li');
        li.textContent = `${data.sid}: ${data.message}`;
        li.className = 'matrix-message';
        messagesList.appendChild(li);
    }
});
