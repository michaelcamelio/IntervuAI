import streamlit as st
from openai import OpenAI
import json

# Load API key directly from file
with open("api_Keys.json", "r") as f:
    my_keys = json.load(f)
openai_api_key = my_keys["open_ai_key"]


# OpenAI Client Configuration
openai_client = OpenAI(api_key=openai_api_key)

# Page Configuration
st.set_page_config(
    page_title="IntervuAI - AI Interview Coach",
    page_icon="🤖",
    layout="wide",
)

st.title("IntervuAI - AI Interview Coach")

# Tabs for different functionalities
coding_tab, behavioral_tab = st.tabs(["Coding Interview", "Behavioral Interview"])

# Coding Interview Tab
with coding_tab:
    st.header("Coding Interview Practice")
    st.write("Write your code below and submit it for AI evaluation.")
    
    code = st.text_area("Enter your code:", "def example():\n    return 'Hello'", height=200)
    
    if st.button("Evaluate Code"):
        if code.strip():
            response = openai_client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": f"Evaluate the following Python code for correctness and efficiency:\n{code}",
                }],
                model="gpt-4o",
            )
            
            st.subheader("AI Feedback:")
            st.write(response.choices[0].message.content.strip())
        else:
            st.error("Please enter some code to evaluate.")

# Behavioral Interview Tab
with behavioral_tab:
    st.header("Behavioral Interview Practice")
    st.write("Answer the following question and receive AI feedback.")
    
    question = "Tell me about a time you faced a challenge at work. How did you handle it?"
    st.subheader("Interview Question:")
    st.write(question)
    
    response_text = st.text_area("Your response:", height=150)
    
    if st.button("Get AI Feedback"):
        if response_text.strip():
            feedback = openai_client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": f"Analyze the following behavioral interview response based on clarity, structure (STAR method), and professionalism:\n{response_text}",
                }],
                model="gpt-4o",
            )
            
            st.subheader("AI Feedback:")
            st.write(feedback.choices[0].message.content.strip())
        else:
            st.error("Please enter your response to get feedback.")

st.write("\n")
st.write("**Note:** This is a simple AI-powered interview coach for practice purposes!")
