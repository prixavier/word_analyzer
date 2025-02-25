# Flask Microservice

from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return "Welcome to the Word Analyzer Microservice!"

# Function to analyze words
def analyze_word(command, word):
    if command == "length":
        return len(word)
    elif command == "vowels":
        return sum(1 for char in word if char in "aeiouAEIOU")
    elif command == "repeats":
        return sum(word.count(char) > 1 for char in set(word))
    else:
        return "Invalid command"

# API route to process requests
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400
        
        command = data.get("command")
        word = data.get("word")

        if not command or not word:
            return jsonify({"error": "Missing command or word"}), 400

        result = analyze_word(command, word)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)
