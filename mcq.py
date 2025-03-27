import streamlit as st
import random
import json
import time

def generate_mcqs(grade, subject):
    # Generate MCQs logic...
    with open(grade+'_'+subject+'.json') as file:
        data = json.load(file)
    subject_questions = data['questions']
    # Check if there are enough questions available
    if len(subject_questions) < 5:
        st.warning("Insufficient questions available for the selected grade and subject.")
        return []

    # Randomly select 10 questions from the subject
    mcqs = random.sample(subject_questions, k=5)

    return mcqs

# Main Streamlit app
def cqmain():
    selected_option: None
    st.title("Your Personal Tutor for Content")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.sidebar.title("Options")

        # Get user inputs for grade and subject
        grade = st.sidebar.selectbox("Select Grade", ["present","Grade 10","Grade 11","Grade 12"])
        subject = st.sidebar.selectbox("Select Subject", ["math","social","physics","biology","chemistry", "present"])
        # Generate MCQs based on user inputs
        generate_mcqs_button = st.sidebar.button("Generate MCQs")
        if generate_mcqs_button:
            mcqs = generate_mcqs(grade, subject)

            # Check if there are enough MCQs available
            if not mcqs:
                st.warning("No MCQs available for the selected grade and subject.")
                return

            # Display the MCQs and get user answers
            st.header("Generated MCQs")
            user_answers = []
            for i, mcq in enumerate(mcqs):
                st.subheader(f"Question {i+1}:")
                st.write(mcq["question"])
                selected_option = st.radio(f"Answer {i+1}:", options=mcq["options"], key=f"answer_{i}")
                user_answers.append(selected_option)

            # Store the user answers in session state
            st.session_state.user_answers = user_answers
            st.session_state.show_score = False

            # Start the session timer
            if "start_time" not in st.session_state:
                st.session_state.start_time = time.time()

            # Submit button to evaluate answers
            submit_button = st.sidebar.button("Submit")
            if submit_button:
                if "user_answers" in st.session_state:
                    user_answers = st.session_state.user_answers

                    # Check if user has answered all the questions
                    if len(user_answers) != len(mcqs):
                        st.warning("Please answer all the questions before submitting.")
                        return

                    score = 0
                    st.session_state.show_score = True

                    # Calculate and display the total score
                    st.header("Result")
                    for i, (mcq, user_answer) in enumerate(zip(mcqs, user_answers)):
                        st.subheader(f"Question {i+1}:")
                        st.write(mcq["question"])
                        st.write(f"Correct Answer: {mcq['answer']}")
                        st.write(f"Your Answer: {user_answer}")
                        if user_answer == mcq["answer"]:
                            score += 1
                    st.sidebar.subheader("Total Score:")
                    st.sidebar.write(f"{score} / {len(mcqs)}")

    with col2:
        if generate_mcqs_button:
            st.header("Session Timer")
            timer_placeholder = st.empty()
            while True:
                elapsed_time = int(time.time() - st.session_state.start_time)
                minutes, seconds = divmod(elapsed_time, 60)
                hours, minutes = divmod(minutes, 60)
                timer_display = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
                timer_placeholder.write(f"Session Timer: {timer_display}")
                time.sleep(1)

if __name__ == "__main__":
    cqmain()
