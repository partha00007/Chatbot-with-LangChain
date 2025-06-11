# main.py

from langchain_ollama import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage

# Initialize the chatbot
llm = OllamaLLM(model="llama3")  # Updated class name!

# Set up the system message
messages = [
    SystemMessage(content="You are a helpful chatbot.")
]

print("🤖 Chatbot is ready! Type 'bye' to exit.\n")

# Interactive loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("🤖 Bot: Goodbye! Have a great day.")
        break

    # Add user's message
    messages.append(HumanMessage(content=user_input))

    # Get bot's response
    response = llm.invoke(messages)

    # Print bot's response
    print("🤖 Bot:", response)

    # Add bot's response to conversation history
    messages.append(SystemMessage(content=response))
