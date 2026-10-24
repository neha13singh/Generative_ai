from dotenv import load_dotenv
load_dotenv()
import os
from typing import TypedDict

#create state first

class pipelineState(TypedDict):
    raw_input:str
    edited_text:str
    script_text:str
    final_output:str


#end-----------------state work--------------------

#loading llm model using openai

from langchain_openai import ChatOpenAI
# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",temperature=0.7
)

#----creating node and node is just a python function
#docstring is """""" is a string which tell ai what is the function of this method or we can say definition of function

def editor_node(state:pipelineState)->dict:
    """ State 1: cleans up grammer, remove typos, and refines the tone."""
    prompt=(
        "You are an expert copyeditor. clean up the following raw text."
        "fix any grammatical errors, spelling mistakes, and smooth out the transition flow"
        "while keeping the core message intact. Return only the edited text\n \n"
       f"text: \n {state['raw_input']}"
    )
    response=llm.invoke(prompt)
    return {"edited_text": response.content.strip()}

def scriptwriter_node(state: pipelineState)->dict:
    """Stage 2: formats the clean text into an engaging video script style."""
    print("\n --- [stage 2] Executing ScriptWriter Node---")
    prompt=(
        "you are a charismatic Youtube content creator. Take this edited text and transform"
         "it into a highly engaging, punchy, conversational video script hook. Make it sound"
         "like a real person speaking passionately. Return only the script content. \n \n"
         f"Edited Text:\n {state['edited_text']}"
        )
    response = llm.invoke(prompt)
    return {"script_text": response.content.strip()}



def translator_node(state: pipelineState)->dict:
    """Stage 3: Translates the script into natural flowing Higlish.."""
    print("\n --- [stage 3] Executing translator_node Node---")
    prompt=(
        "You are an expert content localizer for the Indian Market. Take the following script"
        "and convert it into natural, flowing, 'higlish'. Do no simply transalte it sentence-by sentence"
        "or repeat information. Alternately Comfortably between hindi and english phrase just like "
        "an intellectual tech educator would speak naturally on a live stream"
        "return only the final higlish text. \n \n"
        f"Script:\n {state['script_text']}"
        )
    response = llm.invoke(prompt)
    return {"final_output": response.content.strip()}
#------node creation done---------------------

#next connect these nodes using graph
#now your state and nodes are ready and now it is time to create the graph and edges
#edges _ connection point between nodes
from langgraph.graph import StateGraph, START, END

graph=StateGraph(pipelineState)
#add the nodes in the graph 

graph.add_node("editor",editor_node)
graph.add_node("scriptwriter",scriptwriter_node)
graph.add_node("translator",translator_node)

#add edges means connecting these graphs together with connecting points called eges
#sequential one after another

graph.add_edge(START,"editor")
graph.add_edge("editor","scriptwriter")
graph.add_edge("scriptwriter","translator")
graph.add_edge("translator",END)

#compile the graph 
app=graph.compile()

#now graph is created and this also become a runnable we can invoke it
result=app.invoke(
    {
        "raw_input":"AI Agents is the future of tech. They can think plan and act. Langgraph helps"
    }
)
print(result)
print(result['final_output'])










