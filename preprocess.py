import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("C:\IRIS\JAM\INTERNSHIPS\MS ELEVATE\Copilot\study_data.csv")

print("Initial Dataset Shape:", df.shape)

# Drop student_id (not useful for ML)
df = df.drop(columns=["student_id"])

# Initialize label encoders
label_encoders = {}

categorical_columns = ["subject", "topic", "difficulty", "consistency"]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features & Target
X = df.drop(columns=["recommended_hours"])
y = df["recommended_hours"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", X_train.shape)
print("Testing samples:", X_test.shape)

# Save processed data
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("✅ Data preprocessing completed successfully!")
