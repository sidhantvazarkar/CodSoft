from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    # Greetings
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help you today?"]],
    [r"good (morning|afternoon|evening)", ["Good %1! How can I assist you today?"]],

    # Asking about the chatbot
    [r"what is your name?", ["I'm a simple rule-based chatbot. You can call me Chatbot!"]],
    [r"who created you?", ["I was created by a developer who wanted to learn more about NLP and chatbots."]],
    [r"are you human?", ["No, I am a chatbot created to assist you."]],
    
    # Chatbot's state
    [r"how are you?", ["I'm just a bunch of code, but I'm here to help you!"]],
    [r"are you (happy|sad)?", ["I'm a chatbot. I don't have feelings, but I am here to make you feel good!"]],

    # Conversational responses
    [r"what (can|could) you do?", ["I can respond to basic queries, tell you jokes, and have a simple conversation."]],
    [r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!"]],
    [r"thank you|thanks", ["You're welcome!", "No problem, happy to help!", "Anytime!"]],
    [r"(good|fine|okay|great|awesome)", ["Glad to hear that! How can I assist you further?"]],
    
    # Asking for help
    [r"help", ["Sure, I'm here to help. What do you need assistance with?"]],
    [r"can you help me (.*)", ["I can help you with basic information and answer questions you might have."]],
    
    # Specific questions
    [r"what is (machine learning|deep learning|AI)?", [
        "Machine learning is a field of computer science that uses statistical techniques to give computer systems the ability to 'learn' from data.",
        "Deep learning is a subset of machine learning that uses neural networks with many layers. AI stands for Artificial Intelligence, which encompasses both machine learning and deep learning."
    ]],
    [r"(.*) weather in (.*)", ["I don't have real-time weather data. You can check a weather website or app for the latest information."]],

    # Farewell
    [r"bye|goodbye|quit|exit", ["Goodbye! Have a great day!", "See you later! Stay safe!"]],

    # Default response
    [r"(.*)", ["I'm not sure I understand. Can you please clarify?", "I'm here to learn more. Could you rephrase that?"]]
]

# Initialize the chatbot
chat = Chat(pairs, reflections)

# Function to get a response from the chatbot
def get_response(user_input):
    return chat.respond(user_input)
