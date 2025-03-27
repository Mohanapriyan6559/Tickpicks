import pdfplumber
import streamlit as st
from openai import OpenAI
import io

client = OpenAI(api_key='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')

def search_openai(query, num=5):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=query
    )
    return response.choices[0].text.strip()

def extract_pdf_content(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def generate_title(content):
    # You can use various methods like keyword extraction or simply use the first line as the title
    lines = content.split('\n')
    title = lines[0] if lines else "Untitled"
    return title

def generate_paragraphs(content):
    # Split the content into paragraphs
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
    return paragraphs

def generate_summary(content):
    summary = search_openai("summarize this text and the number of sentences are 5: " + content)
    return summary

def pdfsummerizermain():
    st.title("Idea-File-Compress")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        file_obj = io.BytesIO(uploaded_file.read())
        content = extract_pdf_content(file_obj)
        
        # Generate title, paragraphs, and summary
        title = generate_title(content)
        paragraphs = generate_paragraphs(content)
        summary = generate_summary(content)
        
        # Display generated elements
        st.write("Title:")
        st.write(title)
        st.write("Paragraphs:")
        st.write(paragraphs)
        st.write("Summary:")
        st.write(summary)

if __name__=='__main__':
    pdfsummerizermain()
