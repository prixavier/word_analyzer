import requests

# Read all commands from text file
with open("input.txt", "r") as file:
    commands = [line.strip() for line in file if line.strip()]

# Ensure commands are in the correct format
for command_line in commands:
    if "," not in command_line:
        print(f"Error: Invalid format in input.txt. Expected 'command,word' → {command_line}")
        continue  # Skip invalid lines

    # Extract command and word
    try:
        command, word = map(str.strip, command_line.split(","))
    except ValueError:
        print(f"Error: Invalid format in input.txt. Expected 'command,word' → {command_line}")
        continue

    # API endpoint
    url = "http://127.0.0.1:5000/analyze"

    # Send request
    try:
        response = requests.post(url, json={"command": command, "word": word})
        if response.status_code == 200:
            print(response.json())  # Print valid results
        else:
            print(f"Error: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
