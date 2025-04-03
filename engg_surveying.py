import google.generativeai as genai
import streamlit as st

# Configure API key
genai.configure(api_key="AIzaSyB_6CNc2O9T52n0xWb6PGg6t608GFlXHrM")

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Get user input
ques = st.text_input("Enter text ")

# Check if user has entered something before calling the model
if ques.strip():  # Ensures the input is not empty or just spaces
    response = model.generate_content(ques)
    st.write(response.text)
else:
    st.warning("Please enter a question before submitting.")  # Show warning if input is empty
