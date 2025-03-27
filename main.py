import streamlit as st
from youtube import youmain
from summarize import spmain
from pdfsummerizer import pdfsummerizermain
from front import fmain
from speechtovoice import speech
from ollama import Client
from mcq import cqmain
from bad import bads

#################111111111##########################
client = Client()

# Function for the Llama3.2 Chatbot
def chatbots():
    st.subheader("Tick-pick-AI Chat Interface")
    user_message = st.text_input("Enter your message:", "")

    if st.button("Send"):
        if user_message:
            # Display loading message
            with st.spinner("Tick-pic-AI is thinking..."):
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










#####################################################################################################################
import speech_recognition as sr

def transcribes():
    """Record and transcribe audio from the microphone."""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            st.info("Listening... Speak now!")
            # Listen for the audio input
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=500)
            st.success("Recording complete. Transcribing...")
            # Transcribe using Google's Speech Recognition API
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.WaitTimeoutError:
        st.error("No speech detected. Please try again.")
    except sr.UnknownValueError:
        st.error("Speech was not clear enough. Could not transcribe.")
    except sr.RequestError as e:
        st.error(f"Error connecting to the Speech-to-Text service: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    return None

def speech_to_text_ui():
    """UI for Speech-to-Text functionality."""
    st.title("Speech to Text")
    st.markdown("Click the button below and start speaking. Your speech will be transcribed into text.")

    if st.button("Start Recording"):
        st.info("Preparing to record...")
        with st.spinner("Recording..."):
            transcription = transcribes()
        if transcription:
            st.write("**Transcription:**")
            st.success(transcription)
        else:
            st.warning("No transcription available. Try again.")
##############################################################################################################################3

def main():
    st.title("SMART LERANING AI")
    st.subheader("Your Personalized Tutor")

    # Sidebar for app selection
    st.sidebar.title("Navigation")
    app_selection = st.sidebar.selectbox(
        "Select Service",
        [
            "About",
            "Unlimited Chatbot",
            "Text to Speech",
            "Speech-to-Text",
            "Youtube-Text",
            "Idea-File-Compress",
            "MCQ",
            "HATE SPEECH"
            
            
            
        ]
    )

    # Display selected functionality
    if app_selection == "About":
        fmain()
    elif app_selection == "Text-Shorty":
        spmain()
    elif app_selection == "Youtube-Text":
        youmain()
    elif app_selection == "Idea-File-Compress":
        pdfsummerizermain()
    elif app_selection == "Text to Speech":
        speech()
    elif app_selection == "Speech-to-Text":
        speech_to_text_ui()
    elif app_selection == "Unlimited Chatbot":
        chatbots() 
    elif app_selection=="MCQ":
        cqmain()
    elif app_selection=="HATE SPEECH":
        bads()



if __name__ == "__main__":
    main()

