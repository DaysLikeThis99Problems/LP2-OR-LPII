import random

responses = {
    "greeting": [
        "Hello!", "Hi there!", "Welcome!", "Greetings!"
    ],
    "farewell": [
        "Goodbye!", "See you later!", "Take care!", "Bye for now!", "Catch you later!"
    ],
    "thanks": [
        "You're welcome!", "No problem!", "My pleasure!", "Anytime!", "Glad to help!"
    ],
    "compliment": [
        "Thank you!", "You're too kind!", "That means a lot!"
    ],
    "how_are_you": [
        "I'm doing great, thanks for asking!", "All good here! How about you?",
        "Feeling fantastic!", "I'm always ready to chat!"
    ],
    "question": [
        "That's an interesting question.", "I'll need to think about that.", 
        "Can you be more specific?", "I'm still learning, but I can try to help."
    ],
    "default": [
        "I'm sorry, I didn't understand that.", "Could you please rephrase?",
        "I'm not sure I follow.", "Try saying that a different way!"
    ]
}

def generate_response(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hello", "hi"]):
        return random.choice(responses["greeting"])
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return random.choice(responses["farewell"])
    elif "thank" in user_input:
        return random.choice(responses["thanks"])
    elif any(word in user_input for word in ["how are you", "how's it going"]):
        return random.choice(responses["how_are_you"])
    elif any(word in user_input for word in ["smart", "awesome", "great job", "cool"]):
        return random.choice(responses["compliment"])
    elif "?" in user_input:
        return random.choice(responses["question"])
    else:
        return random.choice(responses["default"])

# Main interaction loop
while True:
    user_input = input("User: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    bot_response = generate_response(user_input)
    print("Bot:", bot_response)
