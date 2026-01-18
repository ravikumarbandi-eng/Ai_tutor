import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyBuYnEZIrWRKsC4Coejyt6h9MT-MZXNrA4")

model = genai.GenerativeModel("gemini-3-flash-preview")

def tutor_response(user_input, subject, topic, difficulty, accuracy):
    prompt = f"""
You are an AI personal tutor.

Student details:
- Subject: {subject}
- Topic: {topic}
- Difficulty level: {difficulty}
- Accuracy: {accuracy}%

Student question:
"{user_input}"

Give a clear, simple, motivating explanation.
If accuracy is low, give improvement tips.
Do not use complex language.
"""

    response = model.generate_content(prompt)
    return response.text
