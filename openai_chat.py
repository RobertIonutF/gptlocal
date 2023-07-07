import openai
import dotenv
import re
import json
import os

class OpenAIChat:
    def __init__(self, instructions="You are a helpful assistant."):
        openai.api_key = dotenv.get_key('.env', 'OPENAI_API_KEY')
        self.requests = []
        self.history = []
        self.instructions = self.init_history(instructions)

    def init_history(self, instructions):
        self.history.append({"role": "system", "content": instructions})
        return instructions  # Return the instructions

    def make_gpt3_request(self, request_message):

        # It needs to be an array of objects like: messages: [{role: "user", content: "Hello, World!"}]
        obj = {"role": "user", "content": request_message}

        # If we have a history, we are going to use that as the context
        if len(self.history) < 1:
            self.history.append(obj)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    obj
                ]
            )
            assistant_response = self.get_message_content(response)
            self.history.append({"role": "assistant", "content": assistant_response})
            return self.history
        else:
            self.history.append(obj)

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=self.history,
            )

            assistant_response = self.get_message_content(response)
            self.history.append({"role": "assistant", "content": assistant_response})
            return self.history

    def clear_history(self):
        self.history.clear()

    def get_message_content(self, response):
        return response['choices'][0]['message']['content']

    def parse_history(self, history):
        messages = []
        for message in history:
            if message["role"] == "system":
                messages.append("System: " + message["content"])
            elif message["role"] == "user":
                messages.append("You: " + message["content"])
            elif message["role"] == "assistant":
                messages.append("Assistant: " + message["content"])
        return messages
    
    def getPrettyHistory(self):
        messages = self.parse_history(self.history)
        for message in messages:
            print(message)

    def save_history(self):
        # we make a gpt3 request to ask for a history suggestion name, we will it use to store the history
        response = self.make_gpt3_request("Please name this conversation history, just write the name and nothing else")
        # we get the name of the history from the response
        history_name = response[-1]["content"]
        # Clean the history name to ensure it's a valid filename
        valid_filename = re.sub('[^a-zA-Z0-9 _-]', '_', history_name)
        # Remove the last item from the history
        self.history.pop()
        self.history.pop()
        # remove all spaces from the valid_name and make it all lowercase
        valid_filename = valid_filename.replace(" ", "").lower()
        with open("history/" + valid_filename + ".json", "w") as outfile:
            json.dump(self.history, outfile)  # Save the history directly
        # we clear the history
        self.clear_history()

    def get_history_files(self):
        # we get all the history files from the history folder
        history_files = os.listdir("history")
        return history_files

    def load_history(self, name):
        # we load the history from the history folder
        try:
            self.clear_history()
            with open("history/" + name) as json_file:
                history = json.load(json_file)
                print(history)
                self.history = history
                print("History loaded!")
        except Exception as e:
            print("Error loading history!")
            print(e)

    def get_history(self):
        return self.history