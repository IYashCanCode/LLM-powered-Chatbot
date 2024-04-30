from streamlit_chat import message
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyBfRzQtaS_d6pDoAx-eU-IqCrfQUBr0_Jo"

chatmodel = ChatGoogleGenerativeAI(model="gemini-pro")

message("""Hey there, great to meet you. I'm Docxer, your personal Question-Answering chatbot.
        
My goal is to help you in finding you answers from your study material.
        
Provide me related document and start a chit chat for accurate and full scoring answers
        
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Talk with Docxer",key='user_input')

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    response = chatmodel(st.session_state.messages)    
    st.session_state.messages.append(AIMessage(content=response.content))

messages = st.session_state.get('messages',[])

for i,j in enumerate(messages):
    if i%2 == 0:
        message(j.content,is_user=True,key = str(i)+'_user')
    else:
        message(j.content,is_user=False,key = str(i)+'_system')

