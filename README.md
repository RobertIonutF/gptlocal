OpenAI Chat
This is a Python project that provides a class OpenAIChat which makes interactions with the OpenAI GPT-3 API easier for chat-based tasks.

The class provides methods for maintaining a conversation history, making GPT-3 requests, parsing the history into a readable format, saving and loading history files, and more.

Features
Create a conversational agent with the OpenAI API.
Manage conversation history and allow chat-based interactions.
Save and load conversation histories to/from files.
Get a list of all saved conversation histories.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/OpenAIChat.git
Move into the project directory:
bash
Copy code
cd OpenAIChat
Install the necessary Python packages:
bash
Copy code
pip install -r requirements.txt
NOTE: The project requires Python 3.6+.

Usage
Firstly, you need to set your OpenAI API key. You can get it from the OpenAI website. Once you have the key, save it in a .env file in your project directory like so:

makefile
Copy code
OPENAI_API_KEY=your-api-key-here
Here is an example of how to use the OpenAIChat class:

python
Copy code
from openai_chat import OpenAIChat

# Instantiate the chat object with the desired system message
chat = OpenAIChat("You are a helpful assistant.")

# Make a GPT-3 request and get the history
history = chat.make_gpt3_request("Hello, World!")
print(history)

# Save the history
chat.save_history()

# Load a specific history file
chat.load_history("your-history-file.json")

# Get all history files
files = chat.get_history_files()
print(files)
Tests
Unit tests are available in the test_openai_chat.py file. Run the tests using the following command:

bash
Copy code
python -m unittest test_openai_chat.py
Contributions
Contributions to this project are welcome! Please create a pull request with your changes.

License
This project is licensed under the terms of the MIT license.