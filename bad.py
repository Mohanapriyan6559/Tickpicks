import streamlit as st

# List of bad words
bad_words = [
             "Fanny", 
             "faded cocks", 
             "Weird wanks",
             "Farted,Bollocks",
             "fuck",
             "bitch",
             "Pussy",
             "mother fucker",
             "son of a bitch",
             "asshole",
             "bad", 
             "cunt",
             "waste piece of shit", 
             "bastard",
             "pervert",
             "womanizer",
             "foursome"
             "gay"
             "lesbian"
             "blow job"
             "naughty",
             "inappropriate", 
             "offensive",
             "ass",
             "dick",
             "DICK",
             ]

# Function to check for bad words
def contains_bad_words(text, bad_words):
    text_lower = text.lower()
    for word in bad_words:
        if word in text_lower:
            return True
    return False

# Function to censor bad words
def censor_bad_words(text, bad_words):
    for word in bad_words:
        text = text.replace(word, '*' * len(word))
    return text

# Streamlit app
def bads():
    st.title("Bad Word Detector and Censor")
    st.write("Enter some text below to check for bad words and censor them.")

    # Text input
    user_input = st.text_area("Enter your text here:")

    if st.button("Check and Censor"):
        if user_input:
            if contains_bad_words(user_input, bad_words):
                st.warning("The text contains bad words!")
                censored_text = censor_bad_words(user_input, bad_words)
                st.success("Censored Text:")
                st.write(censored_text)
            else:
                st.success("The text is clean! No bad words found.")
        else:
            st.error("Please enter some text to check.")

# Run the app
if __name__ == "__main__":
    bads()