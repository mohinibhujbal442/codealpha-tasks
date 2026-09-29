# Task 4: Basic Chatbot

print("🤖 Hello! I am a simple chatbot.")
print("Type 'bye' to exit the chatbot.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: My name is PythonBot.")

    elif user_input == "help":
        print("Bot: You can say hello, ask my name, or ask how I am.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")