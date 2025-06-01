# understanding messages in langchain

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

messages = [
    SystemMessage(content="You are a very professional software developer."),
    HumanMessage(content="Tell me about langchain"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)