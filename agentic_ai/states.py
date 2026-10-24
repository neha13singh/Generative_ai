#common workspace shared between all nodes in langgraph
#understand it as common database for all nodes
#four ways to make states

import os
#first way to create state
#using typed dict common one 

from typing import TypedDict
class State(TypedDict):
    topic:str
    summary:str
    score: str

#this simple state will go to all nodes and interact with this

#_----------------------------------------------------------
#second way to create state is using pydantic model
#pydantic good at data validation and type checking

from pydantic import BaseModel, field_validator

class State(BaseModel):
    topic:str
    score:int
    summary:str ="" #default value
    @field_validator
    def score_positive(cls, v):
        if v<0:
            raise ValueError("score must be positive")
    
#--------------------------------------------------
#third way is python data classes
#standard python data class but it is used very rarely brute force method

from dataclasses import dataclass, field
@dataclass
class State:
    topic:str=""
    summary:str=""
    messages:list=field(default_factory=list)


#----------------------end---------------------------------------------------


#4th method message state using langgraph 

from langgraph.graph import MessagesState
class State(MessagesState):
    user_name=str
    language:str
