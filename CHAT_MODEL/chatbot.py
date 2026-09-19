from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b"
)
messages = [
    SystemMessage(content="You are a funny AI agent")
]

print("--------Enter 0 to exit--------")

while True:
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot : ",response.content)

print(messages)