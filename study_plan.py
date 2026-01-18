import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/rf_model.pkl")

# SAME encoding used during training
subject_map = {
    "DSA": 0,
    "Machine Learning": 1,
    "Python": 2,
    "Databases": 3,
    "Operating Systems": 4
}

topic_map = {
    "Arrays": 0,
    "Linked List": 1,
    "Stack": 2,
    "Queue": 3,
    "Trees": 4,
    "Graphs": 5,
    "Regression": 6,
    "Classification": 7,
    "Clustering": 8,
    "SVM": 9,
    "Neural Networks": 10
}

difficulty_map = {"Easy": 0, "Medium": 1, "Hard": 2}
consistency_map = {"Low": 0, "Medium": 1, "High": 2}

def generate_study_plan(subject, topic, difficulty,
                        quiz_score, time_spent, accuracy, consistency):

    input_data = pd.DataFrame([[
        subject_map.get(subject, 0),
        topic_map.get(topic, 0),
        difficulty_map[difficulty],
        quiz_score,
        time_spent,
        accuracy,
        consistency_map[consistency]
    ]], columns=[
        "subject", "topic", "difficulty",
        "quiz_score", "time_spent", "accuracy", "consistency"
    ])

    predicted_hours = round(model.predict(input_data)[0], 2)

    return {
        "Total Study Hours": predicted_hours,
        "Learning": round(predicted_hours * 0.5, 2),
        "Practice": round(predicted_hours * 0.3, 2),
        "Revision": round(predicted_hours * 0.2, 2)
    }
