from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from pydantic import BaseModel
from typing import List, Optional

from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# Schema for AI using Pydantic
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


# Pydantic parser
parser = PydanticOutputParser(
    pydantic_object=Movie
)


# Streamlit UI
st.title("🎬 Movie Information Extractor")

movie_paragraph = st.text_area(
    "Enter your movie information:",
    height=250,
    placeholder="Paste a movie paragraph here..."
)


# Create ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract the movie information from the paragraph.

{format_instructions}
"""
    ),
    (
        "human",
        "{paragraph}"
    )
])


# Create the model
model = ChatOpenAI(
    model="gpt-4o-mini",
    max_tokens=300
)


# Button
if st.button("🎯 Extract Information"):

    if movie_paragraph:

        with st.spinner("Extracting information..."):

            # Fill the prompt
            formatted_messages = prompt.invoke(
                {
                    "paragraph": movie_paragraph,
                    "format_instructions": parser.get_format_instructions()
                }
            )

            # Send messages to model
            response = model.invoke(formatted_messages)

            # Raw model output
            raw_output = response.content

            # Parse using Pydantic
            parsed_response = parser.parse(raw_output)


        # ---------------- RAW OUTPUT ----------------

        st.subheader("🤖 Raw Model Output")

        st.code(
            raw_output,
            language="json"
        )


        # ---------------- STRUCTURED OUTPUT ----------------

        st.subheader("📦 Structured Output")

        structured_output = parsed_response.model_dump_json(
            indent=4
        )

        st.code(
            structured_output,
            language="json"
        )


    else:
        st.warning("Please enter movie information first.")