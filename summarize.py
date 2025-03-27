
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key='')

def spmain():
    st.title("Text-Shorty")

    # Text input
    text = st.text_area("Enter text to summarize", height=200)

    # Button to generate summary
    if st.button("Generate Summary"):
        # Generate summary using client API
        summary = generate_summary(text)
        st.markdown("## Your Personalized Summary")
        st.write(summary)

def generate_summary(text):
    # Use the client API to generate a summary
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Summarize this text: " + text,
        max_tokens=500  # Adjust the max tokens based on the length of the desired summary
    )
    summary = response.choices[0].text.strip()
    return summary

if __name__ == "__main__":
    spmain()