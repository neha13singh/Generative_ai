from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
#schema for ai using pydantic
class Movie(BaseModel):
    title:str
    release_year : Optional[int]
    genre: List[str]
    director:Optional[str]
    cast:List[str]
    rating:Optional[float]
    summary:str

#pydantic parser to validate data entered by user
parser=PydanticOutputParser(pydantic_object=Movie)




# Streamlit UI
st.title("🎬 Movie Information Extractor")

movie_paragraph = st.text_area(
    "Enter the movie information:",
    height=250,
    placeholder="Paste the movie paragraph here..."
)


# Create ChatPromptTemplate using from_messages()
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an information extraction assistant.

Analyze the movie information provided by the user and extract the most
useful details.

Extract:

1. Movie title
2. Release year
3. Director
4. Main character
5. Main actors
6. Genre
7. Story summary
8. Major themes
9. Important scientific concepts
10. Main message of the movie

Rules:
- Use only the information provided.
- Do not invent information.
- Keep the summary concise.
- Present the answer in a clear and structured format.
"""
    ),
    (
        "human",
        """
Here is the movie information:

{movie}
"""
    )
])


# Create the model
model = ChatOpenAI(
    model="gpt-4o-mini",
    max_tokens=300
)


# Button
if st.button("Extract Information"):

    if movie_paragraph:

        # Fill the {movie} placeholder
        formatted_messages = prompt.invoke(
            {
                "movie": movie_paragraph
            }
        )

        # Send messages to the model
        response = model.invoke(formatted_messages)

        # Display the response
        st.subheader("🎬 Extracted Information")
        st.write(response.content)

    else:
        st.warning("Please enter movie information first.")