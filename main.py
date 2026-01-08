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

loader = PyPDFLoader("LIZARD (3).pdf")
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

{pdf_text}

Try not to talk about stuff that isnt in this document
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
choice = ""
def gen_lizard():
    if choice != "WARIO":
        num = random.randint(1,13)
        if num == 7:
            num = 2
        st.image(f"lizard{num}.jpg")
    else:
        st.image("WAAAAAAAAAAAAAAAAAAAAAA.png","WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
def get_answer(text,name):
  return (get_completion(f"answer the quesion{text}",name))
col2, col3 = st.columns(2)

with col2:
    st.title('**VERY COOL LIZARD WEBSITE!!!**')                              #Webpage starts here!

    st.write("**Talk to the chatbots about lizards!**")
    choice = st.selectbox('Talk to:', ['Lizard', 'Lizard lover',"WARIO"])
    if choice == "WARIO":
      st.image("WAAAAAAAAAAAAAAAAAAAAAA.png","WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      st.title('**VERY COOL WARIO WEBSITE**')

    
    
    name = st.chat_input("ask about lizards here")
    if name:
      st.write(get_answer(name,choice))
    
    submitted2 = st.button('**Re-roll lizards**')
    if submitted2:
      st.error("Re-rollng...")

with col3:
    if choice:
        gen_lizard()
        gen_lizard()
        gen_lizard()
