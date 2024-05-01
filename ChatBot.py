import random

# Defining some basic responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well, how about you?", "All good, thanks for asking!"],
    "what's your name": ["I'm Chatbot.", "You can call me Chatbot."],
    "what is your name": ["I'm Chatbot.", "You can call me Chatbot.",],
    "what are you doing":[" I'm working for you..."],
    "i am also fine":["nice have a great day!"],
    "tell me somthing":["you are looking awesome today and have a good day..\U0001F60A"],
    "tell me a joke":[" of course!.... Why did the golfer bring two pairs of pants?..n case he got a hole in one!\U0001F604","Sure.. Why did the math book look sad? Because it had too many problems! \U0001F604","ok.. is anyone tell you like this? You are loking so beautifull today don't feel i am beautiful because it's a joke \U0001F604"],
    "do you love me":[" ohh so cute...love you too \U0001F917 \U0001F49D"], 
    "default": ["I'm not sure what you mean.", "Could you please clarify?", "I didn't get that."]
}

def respond(message):
    # Check if the message is in responses
    if message.lower() in responses:
        return random.choice(responses[message.lower()])
    else:
        return random.choice(responses["default"])

def chat():
    print("Welcome to the Chatbot!")
    print("You can start chatting. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'quit':
            print("Chatbot: bye! have a good day my dear...!")
            break
        
        reply = respond(user_input)
        print(f"Chatbot: {reply}")

# Start the chatbot
chat()
