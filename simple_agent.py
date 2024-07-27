from langchain.schema import HumanMessage,SystemMessage
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
openai_key = os.getenv("OPEN_API_KEY")

llm_name = "gpt-3.5-turbo"
model = ChatOpenAI(api_key=openai_key,model=llm_name)

messages = [
    SystemMessage(content = "you are computer technician "),
    HumanMessage(content= "how to upgrade ram in my pc")
]
res = model.invoke(messages)
print(res)

