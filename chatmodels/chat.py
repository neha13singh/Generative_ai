from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
# model = init_chat_model("gpt-4o-mini")
# response = model.invoke("Why do parrots talk?")
# # print(model)
# print(response.content)


#method 2
# from langchain_openai import ChatOpenAI
# model=ChatOpenAI(model="gpt-4o-mini", temperature=1,max_tokens=20)
# response=model.invoke("write a poem on ai")
# print(response.content)

# from langchain.chat_models import init_chat_model

# model = init_chat_model("google_genai:gemini-2.5-flash-lite")
# response = model.invoke("Why do parrots talk?")
# print(response.content)


# from langchain_groq import ChatGroq

# model = ChatGroq(
#     model="openai/gpt-oss-20b"
# )

# response = model.invoke("What is cricket in 2 lines only")

# print(response.content)

# from langchain.chat_models import init_chat_model

# model = init_chat_model("openai/gpt-oss-20b", model_provider="groq")
# response = model.invoke("Why do parrots talk?")
# print(response.content)




# from langchain_mistralai import ChatMistralAI

# model = ChatMistralAI(
#     model="mistral-small-latest"
# )

# response = model.invoke("Why do parrots talk?")

# print(response.content)

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="Aleph-Alpha/Kolibri-1",
    max_new_tokens=256,
    temperature=0.7,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Why do parrots talk?")
print(response.content)