import streamlit as st
import simplejson as json
from groq import Groq

# Initialize the Groq client
client = Groq(
    api_key="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",
)

def generate_chat_completion(messages):
    # Generate chat completion
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-70b-8192",
    )
    
    return chat_completion.choices[0].message.content

# Streamlit app layout
st.title("TamJap")

# CSS for styling
st.markdown("""
    <style>
    .chat-box {
        position: fixed;
        bottom: 0;
        width: 100%;
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 5px;
        max-height: 300px;
        overflow-y: auto;
        background-color: white;
    }
    .chat-message {
        margin-bottom: 10px;
    }
    .chat-message.user {
        text-align: right;
        color: blue;
    }
    .chat-message.system {
        text-align: left;
        color: green;
    }
    .floating-button {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Input field for system message
system_message = st.text_input("System Message:")

# Chat input field for user message
user_message = st.chat_input("Type your message here...")

# Check if user has entered a message
if user_message:
    # Add system message to chat history if provided
    if system_message:
        st.session_state.messages.append({"role": "system", "content": system_message})
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_message})
    
    # Generate chat completion and add it to chat history
    response = generate_chat_completion(st.session_state.messages)
    st.session_state.messages.append({"role": "system", "content": response})

# Display chat history
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
for message in st.session_state.messages:
    role_class = "user" if message["role"] == "user" else "system"
    st.markdown(f"<div class='chat-message {role_class}'>{message['content']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
