from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from dotenv import load_dotenv
import os

# Initializin environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initializin socketio 
socketio = SocketIO(app)

# Render template
@app.route("/chat", methods=['GET'])
def chat_page():
    return render_template("index.html")

# Send msg in real time
@socketio.on("message")
def handle_message(msg):
    emit('message', msg, broadcast=True)

# Connect to the server
@socketio.on("connect")
def handle_connect():
    print("Client connected to the server.")

# Disconnect to the server
@socketio.on("disconnect")
def handle_disconnect():
    print("Client has disconnected to the server.")

# Intial page
@app.route("/", methods=['GET'])
def intial_page():
    return "Chat em Tempo Real"

if __name__ == "__main__":

    # Runing app with socketio
    socketio.run(app, debug=True)





