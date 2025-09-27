import os
from openai import OpenAI
from dotenv import load_dotenv


# Load the .env file
load_dotenv()

# Read key from environment
api = os.getenv("OPENAI_API_KEY")

if not api:
    raise ValueError("❌ OPENAI_API_KEY not found. Did you create .env file?")

# Initialize OpenAI client
client = OpenAI(api_key=api)  # Replace with your OpenAI API key

# Small FAQ dictionary (mini RAG)
faq = {
    "What is Python?": "Python is a high-level programming language used for general-purpose programming.",
    "What is Pandas?": "Pandas is a Python library used for data manipulation and analysis.",
    "What is NumPy?": "NumPy is a Python library for numerical computing and working with arrays.",
}

def chatbot(user_input):
    # First, check FAQ
    for key in faq:
        if key.lower() in user_input.lower():
            return faq[key]
    
    # If question not in FAQ, ask OpenAI GPT
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-3.5-turbo
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content

# Main loop
print("Welcome to Python AI Chatbot! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    reply = chatbot(user_input)
    print("Bot:", reply)
    





