from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    SystemMessage,
    HumanMessage
)


st.title("🤖 My AI Chatbot")


tone = st.selectbox(
    "Choose AI tone:",
    ["Funny", "Professional", "Friendly", "Teacher"]
)


tone_prompt = {
    "Funny": "You are a funny AI Agent",
    "Professional": "You are a professional AI Agent",
    "Friendly": "You are a friendly AI Agent",
    "Teacher": "You are a teacher. Explain things simply."
}


# YOUR messages list
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=tone_prompt[tone])
    ]

messages = st.session_state.messages


# Show previous messages
for message in messages:

    if isinstance(message, HumanMessage):
        st.chat_message("user").write(message.content)

    elif isinstance(message, AIMessage):
        st.chat_message("assistant").write(message.content)


# YOUR user input
user = st.chat_input("You:")


if user:

    # YOUR LOGIC
    messages.append(
        HumanMessage(content=user)
    )

    # YOUR MODEL
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=1,
        max_tokens=30
    )

    # YOUR INVOKE
    response = model.invoke(messages)

    # YOUR OUTPUT
    st.chat_message("user").write(user)

    st.chat_message("assistant").write(
        response.content
    )

    # YOUR LOGIC
    messages.append(
        AIMessage(response.content)
    )