import streamlit as st
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
if __name__ == '__main__':
    speech_to_text_ui()