from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
url="https://www.flipkart.com/realme-p4-5g-steel-grey-128-gb/p/itmf836e6de035a5?pid=MOBHN7A8SZ7F9C7T&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InNvdXJjZUNvbnRlbnRUeXBlIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6InNvdXJjZUNvbnRlbnRUeXBlIiwiaW5mZXJlbmNlVHlwZSI6IlNDVCIsInZhbHVlIjoiQUQiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19&nnc=TUP3ZYCOGPA3_AD&pageUID=1791734580160"
data=WebBaseLoader(url)
docs=data.load()
print(len(docs))
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