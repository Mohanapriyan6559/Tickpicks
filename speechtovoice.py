import streamlit as st
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice rate (speed) and volume
engine.setProperty('rate', 150)  # Adjust the value as per your preference
engine.setProperty('volume', 1.0)  # Adjust the value as per your preference

# Streamlit app
def speech():

    st.title("Text to Speech Converter")
    st.image("https://miro.medium.com/v2/resize:fit:1100/format:webp/0*PIm4S-fLsefifYAg.jpeg")
    
    # Input text
    input_text = st.text_area("Enter your text", height=200)
    
    # Convert text to speech
    if st.button("Convert to Speech"):
        if input_text:
            # Save the speech to an audio file
            engine.save_to_file(input_text, 'output.mp3')
            engine.runAndWait()
            
            st.success("Text converted to speech! Click the link below to download the audio file.")
            st.audio('output.mp3', format='audio/mp3')
        else:
            st.warning("Please enter some text to convert.")
    

if __name__ == '__main__':
    speech()
