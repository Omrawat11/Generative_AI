from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b"
)

response = model.invoke(
    "Can you tell me what is machine learning?"
)

print(response.content)