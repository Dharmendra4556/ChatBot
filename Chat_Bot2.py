import streamlit as st
import google.generativeai as genai
from datetime import date

# Streamlit app configuration
st.set_page_config(page_title="ChatBot", page_icon='🤖', layout='centered', initial_sidebar_state='collapsed')

# Use  header to display project name
st.header('🤖ChatBot')
# Initialize session state with model start chat message
if 'chat' not in st.session_state:
    api_key = "AIzaSyBUUejpbU_3eouCT96lkHmkE2mQ6jQb8TU"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.history = []

# Display the chat history
for message in st.session_state.history:
    usr_msg = st.chat_message("user")
    usr_msg.write(message["user"])
    bot_msg = st.chat_message("assistant")
    bot_msg.write(message["bot"])

# Function to add message to history
def add_message(user, bot):
    st.session_state.history.append({"user": user, "bot": bot})

# Function to handle question input and response
def handle_question(question):
    try:
        response = st.session_state.chat.send_message(question)
        add_message(question, response.text)
    except Exception as e:
        st.error(f"Error generating response: {e}")

# Input box for user questions
question = st.chat_input("Say something")
if question:
    handle_question(question)
    st.experimental_rerun()
