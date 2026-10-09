from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
texts=[
    "i am neha",
    "i am 24 years old",
    "i work in google"
]
vector=embedding.embed_documents(texts)
print(vector)