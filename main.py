from openai_chat import OpenAIChat
import os

# Create an instance of the OpenAIChat class
instruction = "You are a helpful assistant."
chat = OpenAIChat(instructions=instruction)

os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print("Hello, this is a chatbot that uses the OpenAI API to generate responses.")
    print("Instructions: " + instruction)
    print("Type 'request' to make a request to the OpenAI API")
    print("Type 'save' to save the history")
    print("Type 'load' to load a history")
    print("Type 'clear' to clear the history")
    print("Type 'exit' to exit the program")

    command = input("Enter a command: ")

    if command == "request":
        chat.getPrettyHistory()
        request = input("Make a request: ")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

        response = chat.make_gpt3_request(request)
        messages = chat.getPrettyHistory()
    elif command == "save":
        chat.save_history()
        print("History saved!")
    elif command == "clear":
        chat.clear_history()
        print("History cleared!")
    elif command == "exit":
        print("Exiting...")
        break
    elif command == "load":
        print("History files: ")
        print(chat.get_history_files())
        file_name = input("Enter the file name: ")
        chat.load_history(file_name)
    else:
        print("Invalid command!")

    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
