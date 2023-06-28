import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

apikey = os.getenv('OPENAI_KEY')

os.environ['OPENAI_API_KEY'] = apikey

# app framework
st.title("LangChain, GPT creator")
prompt = st.text_input("Plug in your prompt here")

# prompt templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='give me a function name for {topic}'
)

code_template = PromptTemplate(
    input_variables=['topic'],
    template="""
        write me a theoretical solution and actual code implementation for this problem,
          explain why you did certain things and how you solved it, add comments to each line of the code implementation,
          code it in node.js/javascript,
          after you're done with the initial solution,
          provide some information about faster solutions and why they're faster, and same thing with slower solutions
          PROBLEM: {topic}
    """
)

#  llms (large language model): https://en.wikipedia.org/wiki/Large_language_model
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template,
                       verbose=True, output_key='title')
code_chain = LLMChain(llm=llm, prompt=code_template,
                      verbose=True, output_key='problem')
sequential_chain = SequentialChain(
    chains=[title_chain, code_chain],
    input_variables=['topic'],
    output_variables=['title', 'problem'],
    verbose=True
)

# show stuff to the screen if prompt provided.
if prompt:
    response = sequential_chain({'topic': prompt})
    st.write(response['title'])
    st.write(response['problem'])
