from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
data = TextLoader("rag/document_loaders/notes.txt")
docs=data.load()
template=ChatPromptTemplate.from_messages(
    [
        ("system","you are a AI that summarizes the text in 100 words"),
        ("human","{data}")
    ]
)
model = ChatOpenAI(
    model="gpt-4o-mini",
    max_tokens=300
)
prompt=template.format_messages(data=docs[0].page_content)
result=model.invoke(prompt)
print("bot: ",result.content)
