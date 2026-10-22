def get_response(user_input):
    """Return a predefined reply based on the user's message."""
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text == "what is your name":
        return "I'm a simple chatbot."
    elif text == "help":
        return "Try saying: hello, how are you, what is your name, or bye."
    elif text in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def chat():
    print("=== Simple Chatbot ===")
    print("Type 'help' for ideas, or 'bye' to quit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        if response == "Goodbye!":
            break


if __name__ == "__main__":
    chat()