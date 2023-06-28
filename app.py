from langchain.llms import OpenAI
import streamlit as st
import streamlit.components.v1 as components
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

apikey = os.getenv('OPENAI_KEY')

os.environ['OPENAI_API_KEY'] = apikey

# app framework
st.title("LangChain, GPT creator")
prompt = st.text_input("Plug in your prompt here")

#  llms (large language model): https://en.wikipedia.org/wiki/Large_language_model
llm = OpenAI(
    temperature=0.9
)

# show stuff to the screen if prompt provided.
if prompt:
    response = llm(prompt)
    st.write(response)
