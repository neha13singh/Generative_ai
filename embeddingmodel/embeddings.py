from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings
embeddings=OpenAIEmbeddings(
     model="text-embedding-3-small",
     dimensions=64
)
texts=[
     "my name is neha",
     "my age is 24 years old",
     "i work in newgen"
]
vector=embeddings.embed_documents(texts)
print(vector)

