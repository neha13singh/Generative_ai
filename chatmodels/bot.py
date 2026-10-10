from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
# messages=[]
# while True:
#     user=input("you: ")
#     messages.append(user)
#     if user=="0":
#         print("i have to break")
#         break
#     if user=="you: 0":
#         print("now i have to break")
#         break
#     model=ChatOpenAI(model="gpt-4o-mini", temperature=1,max_tokens=30)
#     response=model.invoke(messages)
#     print("bot: ",response.content)
#     messages.append(response.content)
# print(messages)

## now i see how messages in langchain works inbuilt using inbuilt messages 


messages=[
    SystemMessage(content="you are a funny AI Agent")
]
while True:
    user=input("you: ")
    messages.append(HumanMessage(content=user))
    if user=="0":
        print("i have to break")
        break
    if user=="you: 0":
        print("now i have to break")
        break
    model=ChatOpenAI(model="gpt-4o-mini", temperature=1,max_tokens=30)
    response=model.invoke(messages)
    print("bot: ",response.content)
    messages.append(AIMessage(response.content))
print(messages)
