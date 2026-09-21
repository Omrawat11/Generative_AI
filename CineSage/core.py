from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Note: 'open-mistral-nemo' and 'open-mistral-7b' are supported on the free tier.
# 'mistral-small-2506' requires a paid Mistral AI subscription tier.
model = ChatMistralAI(model="open-mistral-nemo")

prompt = ChatPromptTemplate.from_messages([
    ("system",
    """
    You are a professional Movie Informational  Extraction Assistant.
    Your task:
    Extract useful structured information from a movie paragraph and present it in a clean readable format.
    Rules:
    - Do NOT add explanations
    - Do Not add extra commentary
    - Follow the exact format
    - If information is missing -> write NULL
    - Keep summary short (2-3 lines max)
    - Do NOT guess unkown facts

    Output format:

    Movie Title:
    Release Year:
    Genre:
    Director:
    Main Cast:
    Setting/Location:
    Plot:
    Themes:
    Ratings:
    Notable Features:

    Short Summary:
    """),
    ('human',
    """
    Extract information from this paragraph:
    {paragraph}
    """)
])

para = input("Tell your paragraph : ")
final_prompt = prompt.invoke({"paragraph" : para})

response = model.invoke(final_prompt)

print(response.content)

