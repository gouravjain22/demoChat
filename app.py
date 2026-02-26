from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React

# Simple AI response logic
def respond_to_query(query):
    query = query.lower()
    
    if "hello" in query or "hi" in query:
        return "Hello! How can I help you today?"
    elif "your name" in query:
        return "I am a simple AI agent running on Python."
    elif "python" in query:
        return "Python is great! Are you learning it?"
    elif "react" in query:
        return "React is awesome for building modern web applications!"
    elif "gourav" in query:
        return "He is nice"

    else:
        return "Sorry, I don't understand that yet."

# API endpoint
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = respond_to_query(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)