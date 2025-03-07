# word_analyzer
CS 361 Microservice for Word Analyze Program

# Word Analyzer Microservice

This microservice processes word-based commands and returns analysis results such as word length, vowel count, and repeated letter count.

---

##  How to Request Data from the Microservice:

To request data, send a **POST request** to the `/analyze` endpoint with a **JSON body** containing a command and a word.

## Example Request (Python)

import requests

url = "http://127.0.0.1:5000/analyze"
data = {"command": "length", "word": "dog"}

response = requests.post(url, json=data)
print(response.json())  # Expected output: {"result": 3} 

## How to Receive Data from Microservice:

The microservice will return a JSON response containing the requested analysis. Below are example responses:

## Example Response (Success)
json

{"result": 3}

Example Response (Error Handling)
If an incorrect format is sent:

json
{"error": "Missing command or word"}

## UML Sequence Diagram:

+------------+        +----------------------+
|  Client    |        | Flask Microservice   |
+------------+        +----------------------+
       |                         |
       |   POST /analyze         |
       | ----------------------->|
       |                         |
       |   Process request       |
       |   (Extract command,      |
       |    analyze word)         |
       |                         |
       |   Return JSON Response   |
       | <-----------------------|
       |                         |
       |   Display Result         |
       |                         |
+------------+        +----------------------+

## 📜 UML Sequence Diagram

Below is a simplified UML sequence diagram showing how the client interacts with the Flask microservice:

![UML Sequence Diagram](docs/UML_Diagram_Word_Analzyer(1).png)


## How to Run the Microservice
1. Start the Flask Server:
   python3 app.py

2. Ensure input.txt has a valid command.
   length,dog

3. Run the Client Script
    python3 client.py



