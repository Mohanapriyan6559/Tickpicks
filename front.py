import streamlit as st
st.set_page_config(layout="wide")

def fmain():
    # Set the title and page layout
   
    page_bg_img="""  
    <style>
    [data-testid="stVerticalBlockBorderWrapper"]{
    </style>
    """

    st.markdown(page_bg_img,unsafe_allow_html=True)
    
    st.title("Welcome to Smart Learning GEN AI")
    st.subheader("About as Smart Learning AI over view")
    
    # Add a subtitle or description
    
    
    st.markdown("""
        ###### Empowering Education with Artificial Intelligence
        
        Welcome to  our AI-EdTech, your ultimate learning companion! Our platform combines the power of artificial intelligence with education to provide you with a personalized and engaging learning experience.
        
        Whether you are a student, teacher, or lifelong learner, AI-EdTech is designed to cater to your unique needs. Our intelligent algorithms analyze your learning patterns, preferences, and performance to offer tailored content, real-time feedback, and personalized recommendations.
        
        ###### Key Features:
        - **Smart Content:** Access a vast library of interactive and high-quality learning materials across various subjects and topics.
        - **Personalized Learning Paths:** Follow customized learning paths based on your strengths, weaknesses, and learning goals.
        - **Intelligent Assessments:** Receive adaptive assessments that dynamically adjust difficulty based on your performance.
        - **Video Summarization:** Our AI algorithms analyze educational videos and generate concise and informative summaries, saving you time and helping you grasp the key concepts efficiently.
        - **Personalized Content:** We understand that every learner is unique. Our AI engine curates personalized learning content based on your interests, learning style, and proficiency level. Say goodbye to one-size-fits-all education!
        - **Adaptive Learning Paths:** Our platform adapts to your progress and learning pace. It intelligently recommends the most suitable learning paths and resources to optimize your learning journey.
        - **Interactive Assessments:** Experience interactive and adaptive assessments that dynamically adjust to your performance, providing targeted feedback and identifying areas for improvement.
        - **Collaborative Learning:** Connect with fellow learners, join study groups, and engage in collaborative learning experiences. Our platform fosters a vibrant community of learners, encouraging knowledge sharing and peer support.
        
        ###### Get Started:
        Simply navigate into the navigation bar to unlock a world of educational opportunities. Start your learning journey today with our AI-EdTech!
        
        Let's embrace the power of AI and transform the way we learn!
    """)
    # Add a separator
    st.markdown("***")
    
    # Add more content or sections as needed
    
    # Sidebar options
   
    # Add navigation links or options in the sidebar
    
if __name__ == "__main__":
    fmain()
