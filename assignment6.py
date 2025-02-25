# import os
# import re
# import json
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/')  # Define a route for the root URL
# def home():
#     return "Welcome to the Word Analyzer Microservice!"

# if __name__ == '__main__':
#     app.run(debug=True)
    
# # Helper functions
# def count_vowels(word):
#     return sum(1 for char in word.lower() if char in "aeiou")

# def count_repeated_letters(word):
#     return sum(word.lower().count(char) - 1 for char in set(word.lower()) if word.lower().count(char) > 1)

# def process_command(command_line):
#     """Process a single command like 'length,dog' and return the result."""
#     try:
#         command, word = command_line.strip().split(',')
#         word = word.strip()

#         if not word.isalpha():
#             return {"error": f"Invalid word: '{word}' contains non-alphabetic characters"}

#         if command == "length":
#             return {"command": "length", "word": word, "result": len(word)}
#         elif command == "vowels":
#             return {"command": "vowels", "word": word, "result": count_vowels(word)}
#         elif command == "repeats":
#             return {"command": "repeats", "word": word, "result": count_repeated_letters(word)}
#         else:
#             return {"error": f"Invalid command: '{command}'"}

#     except ValueError:
#         return {"error": f"Invalid input format: '{command_line.strip()}'"}

# # Function to process text file and return results
# def process_text_file(file_path):
#     """Reads a file, processes commands, and writes output to a result file."""
#     results = []
#     try:
#         with open(file_path, "r") as file:
#             lines = file.readlines()

#         for line in lines:
#             if line.strip():
#                 results.append(process_command(line))

#         # Write results to output file (for pipelines)
#         output_file = file_path.replace(".txt", "_result.json")
#         with open(output_file, "w") as f:
#             json.dump(results, f, indent=4)
        
#         return results
#     except Exception as e:
#         return [{"error": str(e)}]

# # RESTful API: Handle file upload and process it
# @app.route("/analyze-file", methods=["POST"])
# def analyze_file():
#     """Receives a text file, processes it, and returns JSON output."""
#     if "file" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     uploaded_file = request.files["file"]
#     if uploaded_file.filename == "":
#         return jsonify({"error": "Empty file name"}), 400

#     temp_file_path = "uploaded_commands.txt"
#     uploaded_file.save(temp_file_path)

#     results = process_text_file(temp_file_path)
#     return jsonify(results)

# # Run microservice
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=3000)
