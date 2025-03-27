import streamlit as st
from ollama import Client

# Set up the Ollama Client
client = Client()
# Streamlit App Configuration
st.set_page_config(page_title="Llama3.2 Chat", layout="centered")

# Streamlit Title
st.title("Llama3.2 Chat Interface")

# Input for user message
user_message = st.text_input("Enter your message:", "")

if st.button("Send"):
    if user_message:
        # Display loading message
        with st.spinner("Llama3.2 is thinking..."):
            try:
                # Format input as a list of message objects
                messages = [{"role": "user", "content": user_message}]
                
                # Stream responses
                response = client.chat(
                    model="llama3.2",  # Specify the model name
                    messages=messages,  # Corrected to 'messages'
                    stream=True  # Enable streaming
                )
                
                # Initialize response_text to collect output
                response_text = ""
                
                # Placeholder for progressive updates
                text_placeholder = st.empty()

                for chunk in response:
                    # Check if the chunk contains a message with content
                    if chunk.message and chunk.message.content:
                        response_text += chunk.message.content
                        text_placeholder.text(response_text)  # Update text progressively
                    else:
                        st.write("No content in this chunk.")  # Debugging
                    
                # Final display of the complete response
                if response_text:
                    st.success("Response received!")
                else:
                    st.warning("The model did not generate any content.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message before sending.")
