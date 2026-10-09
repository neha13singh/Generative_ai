#method 2
from langchain_openai import ChatOpenAI
model=ChatOpenAI(model="gpt-4o-mini", temperature=1,max_tokens=20)
response=model.invoke("write a poem on ai")
print(response.content)