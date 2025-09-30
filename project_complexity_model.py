import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic data
def generate_project_data(num_samples=100):
    duration = np.random.randint(2, 60, size=num_samples)  # in weeks
    team_size = np.random.randint(1, 50, size=num_samples)
    budget = np.random.randint(10, 2000, size=num_samples)  # in thousands
    dependencies = np.random.randint(0, 30, size=num_samples)
    stakeholders = np.random.randint(1, 20, size=num_samples)

    # Simple logic to assign complexity
    complexity = []
    for d, t, b, dep, s in zip(duration, team_size, budget, dependencies, stakeholders):
        score = (d / 10) + (t / 10) + (b / 200) + (dep / 5) + (s / 4)
        if score < 5:
            complexity.append('Low')
        elif 5 <= score < 10:
            complexity.append('Medium')
        else:
            complexity.append('High')

    return pd.DataFrame({
        'Duration_Weeks': duration,
        'Team_Size': team_size,
        'Budget_K': budget,
        'Dependencies': dependencies,
        'Stakeholders': stakeholders,
        'Complexity': complexity
    })

# Generate data
df = generate_project_data(100)

# Split features and target
X = df[['Duration_Weeks', 'Team_Size', 'Budget_K', 'Dependencies', 'Stakeholders']]
y = df['Complexity']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Example prediction
example_project = [[12, 10, 250, 5, 4]]  # Custom project input
predicted = model.predict(example_project)
print("Predicted Complexity for example project:", predicted[0])