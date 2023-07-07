# OpenAIChat - A Chatbot using OpenAI GPT-4

OpenAIChat is an interactive command-line chatbot using the OpenAI GPT-4. The chatbot uses the GPT-4 model to generate responses to user queries and maintains a history of the conversation. This history can be saved, cleared, or loaded as needed.

## Setup

Follow these steps to get OpenAIChat up and running:

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/your_github_username/openai_chat.git
    cd openai_chat
    ```

2. **Set up a virtual environment** (optional, but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create an .env file** in the root directory of the project and set your OpenAI API key and the model you wish to use:

    ```bash
    OPENAI_API_KEY=your_openai_api_key
    MODEL=model_name
    INSTRUCTION="You are a helpful assistant."
    ```

## Usage

To start the chatbot, run the `main.py` script:

**You'll be presented with a menu:**

    ```bash
    Hello, this is a chatbot that uses the OpenAI API to generate responses.
    Instructions: You are a helpful assistant.
    Type 'request' to make a request to the OpenAI API
    Type 'save' to save the history
    Type 'load' to load a history
    Type 'clear' to clear the history
    Type 'exit' to exit the program
    ```

## Here's what each command does:

    ```bash
        request: Allows you to make a request to the OpenAI API. Enter your query after issuing this command.
        save: Saves the current chat history in a JSON file.
        load: Loads a previous chat history from a JSON file. You'll need to enter the file name.
        clear: Clears the current chat history.
        exit: Exits the program.
    ```

# Tests
To run tests, use the following command:
    ```bash
        python -m unittest
    ```

# License

License
MIT License

Copyright (c) 2023 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


This includes sections for your project title, description, setup instructions, usage, testing, and license information.
