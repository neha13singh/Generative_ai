from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings
embeddings=OpenAIEmbeddings(
     model="text-embedding-3-small",
     dimensions=64
)

vector=embeddings.embed_query("hello my name is neha")
print(vector)

