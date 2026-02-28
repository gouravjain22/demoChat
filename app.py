from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)
# Allow all origins (for development)
CORS(app, resources={r"/*": {"origins": "*"}})

# Simple in-memory conversation store
conversation_history = []

def detect_intent(query):
    query = query.lower()

    if any(word in query for word in ["hello", "hi", "hey"]):
        return "greeting"
    elif "your name" in query:
        return "identity"
    elif "python" in query:
        return "python"
    elif "react" in query:
        return "react"
    elif "gourav" in query:
        return "person"
    elif "time" in query:
        return "time"
    else:
        return "unknown"


def generate_response(intent, query):
    responses = {
        "greeting": [
            "Hello! 👋",
            "Hi there! How can I assist you?",
            "Hey! Nice to see you."
        ],
        "identity": [
            "I am your AI assistant built with Flask.",
            "I'm a smart AI agent running on Python."
        ],
        "python": [
            "Python is powerful for backend and AI development.",
            "Python is widely used for web, automation and ML."
        ],
        "react": [
            "React is great for building scalable UI.",
            "React makes frontend development efficient and component-driven."
        ],
        "person": [
            "Gourav sounds like a good person 😄"
        ],
        "time": [
            f"The current time is {datetime.now().strftime('%H:%M:%S')}"
        ],
        "unknown": [
            "Hmm... I am still learning. Can you rephrase that?",
            "Interesting question! I'm not trained for that yet."
        ]
    }

    return random.choice(responses[intent])


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    intent = detect_intent(user_message)
    response_text = generate_response(intent, user_message)

    # Save conversation
    conversation_history.append({
        "user": user_message,
        "intent": intent,
        "response": response_text,
        "timestamp": datetime.now().isoformat()
    })

    return jsonify({
        "response": response_text,
        "intent": intent,
        "history_length": len(conversation_history)
    })


@app.route("/api/history", methods=["GET"])
def history():
    return jsonify(conversation_history)


if __name__ == "__main__":
    app.run(debug=True)