import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

# Create output directory if it doesn't exist
os.makedirs('../output', exist_ok=True)

# Step 1: Read the CSV file
print("📖 Reading student data...")
df = pd.read_csv('../data/students.csv')
print(f"✅ Loaded {len(df)} student records\n")

# Display first few records
print("First 5 students:")
print(df.head())
print("\n")

# Step 2: Create Pass/Fail labels based on CGPA
# CGPA >= 6.0 = Pass, CGPA < 6.0 = Fail
print("📊 Creating Pass/Fail labels...")
df['status'] = df['cgpa'].apply(lambda x: 'Pass' if x >= 6.0 else 'Fail')

# Convert Pass/Fail to binary (1 = Pass, 0 = Fail) for ML model
df['label'] = df['cgpa'].apply(lambda x: 1 if x >= 6.0 else 0)

print("CGPA Distribution:")
print(f"Pass (CGPA >= 6.0): {len(df[df['status'] == 'Pass'])} students")
print(f"Fail (CGPA < 6.0): {len(df[df['status'] == 'Fail'])} students")
print("\n")

# Step 3: Prepare data for Machine Learning
print("🤖 Training Machine Learning Model...")
X = df[['cgpa']].values  # Features (CGPA)
y = df['label'].values   # Target (Pass=1, Fail=0)

# Split data into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%\n")

# Step 6: Predict for all students
print("🔮 Predicting Pass/Fail for all students...")
df['predicted_label'] = model.predict(X)
df['predicted_status'] = df['predicted_label'].apply(lambda x: 'Pass' if x == 1 else 'Fail')

# Step 7: Save results to new CSV file
print("💾 Saving results...")
result_df = df[['bt_id', 'name', 'cgpa', 'predicted_status']]
result_df.to_csv('../output/result.csv', index=False)

print("✅ Results saved to output/result.csv\n")

# Display results
print("=" * 60)
print("PREDICTION RESULTS")
print("=" * 60)
print(result_df.to_string(index=False))
print("\n")

# Summary Statistics
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Total Students: {len(df)}")
print(f"Predicted Pass: {len(df[df['predicted_status'] == 'Pass'])}")
print(f"Predicted Fail: {len(df[df['predicted_status'] == 'Fail'])}")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("=" * 60)
print("\n✅ Project completed successfully!")
