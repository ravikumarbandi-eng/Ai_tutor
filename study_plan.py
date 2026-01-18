import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Train model dynamically
def train_model():
    df = pd.read_csv("study_data.csv")

    # Encoding
    df["subject"] = df["subject"].astype("category").cat.codes
    df["topic"] = df["topic"].astype("category").cat.codes
    df["difficulty"] = df["difficulty"].map({"Easy":0,"Medium":1,"Hard":2})
    df["consistency"] = df["consistency"].map({"Low":0,"Medium":1,"High":2})

    X = df.drop(columns=["recommended_hours","student_id"])
    y = df["recommended_hours"]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model

# Cache model so it trains only once
model = train_model()

def generate_study_plan(subject, topic, difficulty,
                        quiz_score, time_spent, accuracy, consistency):

    subject_code = 0
    topic_code = 0

    difficulty_map = {"Easy":0,"Medium":1,"Hard":2}
    consistency_map = {"Low":0,"Medium":1,"High":2}

    input_df = pd.DataFrame([[
        subject_code,
        topic_code,
        difficulty_map[difficulty],
        quiz_score,
        time_spent,
        accuracy,
        consistency_map[consistency]
    ]], columns=[
        "subject","topic","difficulty",
        "quiz_score","time_spent","accuracy","consistency"
    ])

    hours = round(model.predict(input_df)[0], 2)

    return {
        "Total Study Hours": hours,
        "Learning": round(hours * 0.5, 2),
        "Practice": round(hours * 0.3, 2),
        "Revision": round(hours * 0.2, 2)
    }
