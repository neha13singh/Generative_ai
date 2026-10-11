#external data source ko llm se connect krna aur dono ko milke kaam krna hi rag hai
#step1 user upload study material
#step2 document loading
#step3 text splitting 
#step4 embedding generation
#step5 vector database storage
#step6 user ask a question
#step7 Query embedding of question
#step8 similarity search in our stored vector database
#step9 Retriever component : select similarity result of valued data
#step10: given to llm the retrieved similarity chunks or data and then llm gives answer
from dotenv import load_dotenv
load_dotenv()
