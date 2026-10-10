from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# Take movie information from the user
movie_paragraph = input("Enter the movie information: ")


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


# # Fill the {movie} placeholder
# formatted_messages = prompt.format_messages(
#     movie=movie_paragraph
# )
formatted_messages=prompt.invoke(
    {
        "movie":movie_paragraph
    }
)


# Send messages to the model
response = model.invoke(formatted_messages)




# Print the response
print("\nBOT:")
print(response.content)