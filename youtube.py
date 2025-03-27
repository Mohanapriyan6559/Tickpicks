import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        st.error(f"Error: {str(e)}")

def get_subtitles(video_id):
    try:
        subtitles = YouTubeTranscriptApi.get_transcript(video_id)
        return subtitles
    except Exception as e:
        st.error(f"Error: {str(e)}")

def display_transcript(transcript):
    # Join segments of text into a single string separated by newline characters
    transcript_text = '\n'.join([segment['text'] for segment in transcript])
    # Wrap the entire transcript text within a <p> tag
    st.markdown(f"<p>{transcript_text}</p>", unsafe_allow_html=True)

def display_subtitles(subtitles):
    # Join subtitle texts into a single string separated by newline characters
    subtitles_text = '\n'.join([subtitle['text'] for subtitle in subtitles])
    # Wrap the entire subtitles text within a <p> tag
    st.markdown(f"<p>{subtitles_text}</p>", unsafe_allow_html=True)

def youmain():
    st.title("Transcript Viewer")
    st.image("https://i.ytimg.com/vi/BDJWOSQ54gg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCxOK2K_KTdtDaB7Wm5lmt5FQ1fXQ")

    video_id = st.text_input("Enter YouTube Video ID")

    if st.button("Get Transcript"):
        if video_id:
            transcript = get_transcript(video_id)
            if transcript:
                display_transcript(transcript)
        else:
            st.warning("Please enter a YouTube Video ID")

    if st.button("Get Subtitles"):
        if video_id:
            subtitles = get_subtitles(video_id)
            if subtitles:
                display_subtitles(subtitles)
        else:
            st.warning("Please enter a YouTube Video ID")

if __name__ == "__main__":
    youmain()