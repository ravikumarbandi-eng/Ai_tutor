import streamlit as st
import google.generativeai as genai

# Read API key from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-3-flash-preview")

def tutor_response(user_input, subject, topic, difficulty, accuracy):
    prompt = f"""
You are an AI personal tutor.

Student context:
Subject: {subject}
Topic: {topic}
Difficulty: {difficulty}
Accuracy: {accuracy}%

Student question:
{user_input}

Give a clear, more explanation.
If accuracy is low, suggest improvements.
Keep the response large and motivating.
"""

    response = model.generate_content(prompt)
    return response.text


