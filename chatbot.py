def chatbot():
    print("Hello! I'm ChatBot. How can I help you today?")
    print("You can ask me questions like:\n - 'Hii'\n - 'What is your name?'\n - 'What can you do?'\n - 'How is the weather?'\n - 'Tell me a joke.'\n - 'Exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if "Hii" in user_input:
            print("ChatBot: Hii , How can i help you !!")
        elif "your name" in user_input:
            print("ChatBot: I'm ChatBot! Your virtual assistant.")
        elif "what can you do" in user_input:
            print("ChatBot: I can chat with you, tell jokes, and answer simple questions!")
        elif "weather" in user_input:
            print("ChatBot: I'm not connected to the internet, but it looks sunny in here!")
        elif "joke" in user_input:
            print("ChatBot: Why don't scientists trust atoms? Because they make up everything!")
        elif "exit" in user_input:
            print("ChatBot: Goodbye! Have a great day!")
            break
        else:
            print("ChatBot: I'm sorry, I didn't understand that. Can you ask something else?")

# Run the chatbot
chatbot()
