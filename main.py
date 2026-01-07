# @title Create main.py

from openai import OpenAI
import streamlit as st
from getpass import getpass
import random
from langchain_community.document_loaders import PyPDFLoader
import tiktoken # Import tiktoken

# Define the count_tokens function
def count_tokens(text):
    encoding = tiktoken.get_encoding("cl100k_base") # or another appropriate encoding
    return len(encoding.encode(text))

loader = PyPDFLoader("LIZARD (1).pdf")
pages = loader.load()
import numpy as np

list_of_tokencounts = []
for page in pages:
    # Count the tokens in the content of each page
    # then append the count to the list
    list_of_tokencounts.append(count_tokens(page.page_content))

# Sum the token counts from all pages

pdf_text = "\n\n".join([page.page_content for page in pages])
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
def get_completion(user_prompt, persona, model="gpt-4o-mini"):
    system_prompt = f"""
You are roleplaying as: {persona}

You must follow the rules and knowledge found in the following document:

{pdf_text}

Use this document as the absolute source of truth.
If the answer is not in the document, say you don't know.
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.1,
    )

    return response.choices[0].message.content

def gen_lizard():
    num = random.randint(1,13)
    st.image("lizard{num}.jpg")
def get_answer(text,name):
  return (get_completion(f"answer the quesion{text}",name))
col1, col2, col3 = st.columns(3)
with col1:
    gen_lizard()
    gen_lizard()
    gen_lizard()
with col2:
    st.title('**VERY COOL LIZARD WEBSITE!!!**')                              #Webpage starts here!

    st.write("**You love lizards, don't you?**")
    submitted2 = st.button('**The above information is false.**')
    if submitted2:
      st.error("How dare you?!")
    choice = st.selectbox('Talk to:', ['Lizard', 'Lizard lover',"WARIO"])
    if choice == "WARIO":
      st.image("WAAAAAAAAAAAAAAAAAAAAAA.png","WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      st.title('**VERY COOL WARIO WEBSITE**')

    
    
    name = st.chat_input("ask about lizards here")
    if name:
      st.write(get_answer(name,choice))
    

with col3:
    gen_lizard()
    gen_lizard()
    gen_lizard()
