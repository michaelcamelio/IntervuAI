import streamlit as st
import json
from openai import OpenAI

# Load API keys securely
def load_api_key(filepath="api_Keys.json", key_name="open_ai_key"):
    try:
        with open(filepath, "r") as f:
            keys = json.load(f)
        return keys.get(key_name)
    except FileNotFoundError:
        st.error("API key file not found.")
        return None
    except json.JSONDecodeError:
        st.error("Error decoding the API key file.")
        return None

# Initialize OpenAI client
api_key = load_api_key()
if api_key:
    openai_client = OpenAI(api_key=api_key)
else:
    st.stop()

# Configure Streamlit page
st.set_page_config(
    page_title="IntervuAI - AI Interview Coach",
    layout="wide",
)

st.title("IntervuAI - AI Interview Coach")

# Set up tabs for different interview types
coding_tab, behavioral_tab = st.tabs(["Coding Interview", "Behavioral Interview"])

# --- Coding Interview Tab ---
with coding_tab:
    st.header("Coding Interview Practice")
    st.write("Write your code below and submit it for AI evaluation.")
    
    code_input = st.text_area("Enter your code:", "def example():\n    return 'Hello'", height=200)
    
    if st.button("Evaluate Code"):
        if code_input.strip():
            try:
                response = openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "user", "content": f"Evaluate the following Python code for correctness and efficiency:\n{code_input}"}
                    ],
                )
                st.subheader("AI Feedback:")
                st.write(response.choices[0].message.content.strip())
            except Exception as e:
                st.error(f"An error occurred while evaluating the code: {str(e)}")
        else:
            st.warning("Please enter some code to evaluate.")

# --- Behavioral Interview Tab ---
with behavioral_tab:
    st.header("Behavioral Interview Practice")
    st.write("Answer the following question and receive AI feedback.")
    
    question = "Tell me about a time you faced a challenge at work. How did you handle it?"
    st.subheader("Interview Question:")
    st.write(question)
    
    behavioral_response = st.text_area("Your response:", height=150)
    
    if st.button("Get AI Feedback"):
        if behavioral_response.strip():
            try:
                feedback = openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "user", "content": f"Analyze the following behavioral interview response based on clarity, structure (STAR method), and professionalism:\n{behavioral_response}"}
                    ],
                )
                st.subheader("AI Feedback:")
                st.write(feedback.choices[0].message.content.strip())
            except Exception as e:
                st.error(f"An error occurred while analyzing the response: {str(e)}")
        else:
            st.warning("Please enter your response to get feedback.")

# Footer Note
st.markdown("---")
st.markdown("**Note:** This is a simple AI-powered interview coach for practice purposes.")
