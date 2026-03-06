import os
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = "gsk_groq_api_key_goes_here"

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
    timeout=30,      # Give up after 30 seconds
    max_retries=2,   # Don't retry indefinitely
)

prompt = "Write an email to my supervisor requesting leave."

response = llm.invoke(prompt)

print(response.content)
