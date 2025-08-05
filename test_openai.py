from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

response = model.invoke("Hello, can you hear me?")
print("Response:", response.content)
