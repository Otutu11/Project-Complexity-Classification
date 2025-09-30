import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Sample synthetic data
data = {
    'Duration_Weeks': [4, 12, 24, 36, 8, 52, 16, 20, 6, 30],
    'Team_Size': [3, 10, 20, 25, 5, 30, 12, 15, 4, 22],
    'Budget_K': [20, 100, 300, 500, 50, 1000, 200, 250, 30, 400],
    'Dependencies': [1, 4, 10, 15, 2, 20, 6, 8, 1, 12],
    'Stakeholders': [2, 5, 8, 10, 3, 15, 6, 7, 2, 9],
    'Complexity': ['Low', 'Medium', 'High', 'High', 'Low', 'High', 'Medium', 'Medium', 'Low', 'High']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[['Duration_Weeks', 'Team_Size', 'Budget_K', 'Dependencies', 'Stakeholders']]
y = df['Complexity']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model training
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Classification Report:\n", classification_report(y_test, y_pred))

# Example prediction
new_project = [[10, 8, 120, 3, 4]]  # Change values as needed
predicted_complexity = model.predict(new_project)
print("Predicted Project Complexity:", predicted_complexity[0])