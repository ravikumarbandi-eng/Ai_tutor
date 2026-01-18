import streamlit as st
from study_plan import generate_study_plan
from tutor_bot import tutor_response


# Page config
st.set_page_config(page_title="AI Personal Tutor", layout="wide",text-align:"centre")

st.title("🎓 AI Study Planner & Chatbot")

# ---------------- SIDEBAR ----------------
st.sidebar.header("👤 Student Profile")

subject = st.sidebar.text_input("Subject Name"
)

topic = st.sidebar.text_input("Topic Name")

difficulty = st.sidebar.selectbox(
    "Difficulty Level",
    ["Easy", "Medium", "Hard"]
)

quiz_score = st.sidebar.slider("Quiz Score (%)", 40, 100, 70)
time_spent = st.sidebar.slider("Time Spent (minutes)", 20, 180, 60)
accuracy = st.sidebar.slider("Accuracy (%)", 50, 100, 75)
consistency = st.sidebar.selectbox(
    "Consistency Level",
    ["Low", "Medium", "High"]
)

# ---------------- MAIN SECTION ----------------
st.subheader("📅 AI-Generated Study Plan")

if st.button("Generate Study Plan"):
    plan = generate_study_plan(
        subject, topic, difficulty,
        quiz_score, time_spent, accuracy, consistency
    )

    st.success("✅ Study Plan Generated!")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Hours", f"{plan['Total Study Hours']} hrs")
    col2.metric("Learning", f"{plan['Learning']} hrs")
    col3.metric("Practice", f"{plan['Practice']} hrs")
    col4.metric("Revision", f"{plan['Revision']} hrs")

# ---------------- CHATBOT ----------------
st.subheader("🤖 AI Tutor Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_message = st.text_input("Ask your tutor:")

if st.button("Send"):
    if user_message:
        bot_reply = tutor_response(
            user_message,
            subject,
            topic,
            difficulty,
            accuracy
        )

        st.session_state.chat.append(("You", user_message))
        st.session_state.chat.append(("Tutor", bot_reply))

for speaker, msg in st.session_state.chat:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Tutor:** {msg}")



