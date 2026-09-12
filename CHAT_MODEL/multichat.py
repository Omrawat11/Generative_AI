from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")

print("----Welcome to the chat world----")
print("Select model types:- ")
print("Press 1 for Angry mode")
print("Press 2 for Sad mode")
print("Press 3 for funny mode")

choice = int(input("Tell your response:- "))
if choice ==1:
    mode = "You are an Angry AI agent. you respond in angry way"
elif choice ==2:
    mode = "You are an Sad AI agent. you respond in sad way"
elif choice ==3:
    mode = "You are an Funny AI agent. you respond in funny way"

messages = [
    SystemMessage(content=mode)
]

print("------Press 0 to exit------")
while True:
    prompt = input("You:- ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot:- ",response.content)
print(messages)