#vector store
import getpass

from dotenv import load_dotenv
load_dotenv()
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document


from langchain_openai import OpenAIEmbeddings

docs = [
    Document(
        page_content="Python is widely used for AI and machine learning.\nIt is popular because of its simple syntax.",
        metadata={"source": "book"}
    ),
    Document(
        page_content="Hi Neha, your interview is scheduled for Monday.\nPlease confirm your availability by tomorrow.",
        metadata={"source": "mail"}
    ),
    Document(
        page_content="LangChain helps developers build applications using LLMs.\nIt supports document loading, retrieval, and prompt management.",
        metadata={"source": "documentation"}
    )
]
embedding_model=OpenAIEmbeddings()
vectorstore=Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

result=vectorstore.similarity_search("what is langchain?",k=1)
for r in result:
    print(r)

retriever=vectorstore.as_retriever()
docs=retriever.invoke("explain deep learning?")
for d in docs:
    print(d.page_content)
