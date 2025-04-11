INTERVIUAI

This project contains the source code for IntervuAI, an AI-powered interview preparation tool built using Python, Streamlit, and OpenAI's GPT-4o API.

*How to Set Up and Run the Project*

1. Prerequisites

Python 3.8 or higher

pip (Python package installer)

2. Installation Steps

Clone the Repository

git clone https://github.com/your-username/intervuai.git
cd intervuai

Install Dependencies

pip install streamlit openai

Configure API Keys

Create a file named api_Keys.json in the root folder and add your OpenAI key:

{
  "open_ai_key": "your_openai_api_key_here"
}

Note: Do not commit this file to source control.

3. Running the App

Run the following command in the project directory:

streamlit run app.py

Then open the application in your browser at:

http://localhost:8501

File Overview

app.py: Main application file

api_Keys.json: Contains OpenAI API key (user-provided)

README.md: Setup and usage instructions

Notes

The app includes two main features: coding interview evaluation and behavioral interview analysis.

All evaluations are powered by the GPT-4o model.

This tool is for academic and practice use only.