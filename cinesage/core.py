from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


# Movie information
movie_paragraph = """
Interstellar is a 2014 science-fiction film directed by Christopher Nolan.
The story is set in a future where Earth is suffering from severe environmental
problems, making it increasingly difficult for humans to survive. Former NASA
pilot Cooper is recruited for a secret space mission to search for a new
habitable planet beyond a wormhole near Saturn. Along with a team of astronauts,
he travels through the wormhole and explores distant worlds while facing the
effects of gravity, time dilation, black holes, and relativity.

One of the film's central ideas is that time can pass differently depending
on gravity and speed, meaning that only a few hours for the astronauts can
correspond to many years on Earth. The movie also explores the relationship
between science, human survival, love, sacrifice, and the bond between a
parent and child.
"""


# Create PromptTemplate
prompt = PromptTemplate.from_template("""
You are an information extraction assistant.

Analyze the following movie information and extract the most useful details.

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

Movie Information:
{movie}
""")


# Create the model
model = ChatOpenAI(
    model="gpt-4o-mini",
    max_tokens=300
)


# Fill the prompt with movie information
formatted_prompt = prompt.format(
    movie=movie_paragraph
)


# Send prompt to the model
response = model.invoke(formatted_prompt)


# Print the response
print("BOT:")
print(response.content)