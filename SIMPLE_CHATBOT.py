# SET ENVORIMENT
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv("C:\LANGCHAIN\.env")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

from langchain_community.llms import Ollama

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#  prompt templet

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Your a assistant for user and Give Best answer of every question of user",
        ),
        ("user", "Question:{Question}"),
    ]
)

#  streamlit

st.title("CHAT BOT USING gamma2")

input_text = st.text_input("WHAT I CAN HELP YOU ?")
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"Question": input_text}))
