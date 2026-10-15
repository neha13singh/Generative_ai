from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


docs = [
    Document(
        page_content="""
        Retrieval-Augmented Generation (RAG) combines information
        retrieval with text generation. It retrieves relevant
        information from external documents and provides it as
        context to a Large Language Model (LLM). This helps the
        model answer questions using a specific knowledge base.
        RAG pipelines commonly include document loading, chunking,
        embeddings, vector storage, retrieval, and response generation.
        """,
        metadata={
            "id": "AI001",
            "topic": "RAG",
            "source_type": "documentation",
            "category": "Generative AI"
        }
    ),

    Document(
        page_content="""
        Large Language Models (LLMs) are deep learning models
        trained on large amounts of text data. They can perform
        tasks such as summarization, question answering, translation,
        and code generation. LLMs generate text by predicting tokens
        based on the input context. However, they can sometimes
        generate incorrect information, a problem commonly called
        hallucination. Examples of LLM families include GPT, Llama,
        and Gemini.
        """,
        metadata={
            "id": "AI002",
            "topic": "Large Language Models",
            "source_type": "textbook",
            "category": "Generative AI"
        }
    ),

    Document(
        page_content="""
        Embeddings are numerical vector representations of text.
        They capture semantic relationships between words, sentences,
        and documents. Texts with similar meanings often have vectors
        that are close together in the embedding space. Embeddings
        are widely used for semantic search, document retrieval,
        clustering, and recommendation systems. In a RAG application,
        each document chunk is converted into an embedding before
        being stored in a vector database.
        """,
        metadata={
            "id": "AI003",
            "topic": "Text Embeddings",
            "source_type": "technical_note",
            "category": "Machine Learning"
        }
    ),

    Document(
        page_content="""
        A vector database stores vector embeddings along with
        associated information such as document text and metadata.
        When a user submits a query, the query can be converted into
        an embedding and compared with stored vectors. Similarity
        measures such as cosine similarity help identify relevant
        results. ChromaDB is a vector database that can be integrated
        with LangChain to build semantic search and RAG applications.
        Metadata filtering can further restrict results to specific
        topics, sources, or categories.
        """,
        metadata={
            "id": "AI004",
            "topic": "Vector Databases",
            "source_type": "technical_documentation",
            "category": "RAG"
        }
    ),

    Document(
        page_content="""
        Prompt engineering involves designing clear instructions
        for a Large Language Model. A well-designed prompt can
        specify the task, provide background context, define the
        expected output format, and establish constraints. Prompt
        templates allow applications to insert dynamic values such
        as user questions and retrieved documents. LangChain provides
        prompt template components that help developers organize
        inputs consistently. Effective prompts can improve the
        usefulness of responses, although they cannot guarantee
        factual accuracy.
        """,
        metadata={
            "id": "AI005",
            "topic": "Prompt Engineering",
            "source_type": "learning_material",
            "category": "Generative AI"
        }
    ),

    Document(
        page_content="""
        An AI agent is a system that uses a language model to decide
        how to perform a task and interact with available tools.
        Tools may include calculators, search engines, APIs, and
        databases. A typical agent receives a request, selects an
        action, observes the result, and decides what to do next.
        LangChain supports the development of applications that
        combine language models with tools. Agents can automate
        multi-step workflows, but they require appropriate permissions,
        error handling, and execution limits to operate reliably.
        """,
        metadata={
            "id": "AI006",
            "topic": "AI Agents",
            "source_type": "technical_article",
            "category": "Agentic AI"
        }
    )
]

# print("Total documents:", len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)
embeddings=HuggingFaceBgeEmbeddings()

vectorstore=Chroma.from_documents(docs,embeddings)
retriever=vectorstore.as_retriever()
llm=ChatOpenAI( model="gpt-4o-mini")
Multi_query_retriever=MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=llm
)
query="what is llm?"

docs=Multi_query_retriever.invoke(query)

print("\n Retrieved Documents \n")
for doc in docs:
    print(doc.page_content)