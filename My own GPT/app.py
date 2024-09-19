import streamlit as st
from main import generate_response

# Set up the app title and description
st.title('GPT-powered Chatbot')
st.write('This app is powered by GPT and allows you to interact with it in a conversational format.')

# Initialize the session state to store the conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Create a text input for user queries with a placeholder
user_input = st.text_input('Enter your message:', '')

# Create a button that triggers the response generation
if st.button('Send'):
    if user_input:
        # Add the user's message to the conversation
        st.session_state.conversation.append({'role': 'user', 'content': user_input})

        # Generate GPT response and add it to the conversation
        response = generate_response(user_input)
        st.session_state.conversation.append({'role': 'assistant', 'content': response})

        # Clear the input field
        st.experimental_rerun()
    else:
        st.write('Please enter a message.')

# Display the conversation in a chat format
for message in st.session_state.conversation:
    if message['role'] == 'user':
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**GPT:** {message['content']}")
