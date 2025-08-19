# Project Complexity Classification

This project is a machine learning-based system to classify software or business projects into **Low**, **Medium**, or **High** complexity based on several features.

## 🔍 Features

Each project is defined by the following attributes:

- `Duration_Weeks`: Duration of the project in weeks.
- `Team_Size`: Number of people involved in the project.
- `Budget_K`: Budget in thousands of dollars.
- `Dependencies`: Number of external/internal dependencies.
- `Stakeholders`: Number of stakeholders involved.

The target label is `Complexity`, which can be:
- `Low`
- `Medium`
- `High`

## 🧠 Model

A **Decision Tree Classifier** is trained on synthetic data generated using realistic ranges and a scoring formula. The model predicts the complexity level of a project based on its features.

## 📁 Files

- `project_complexity_classifier.py` — Python script with data generation, model training, and evaluation.
- `project_complexity_data.xlsx` — Excel file containing synthetic project data.
- `README.md` — This file.

## 📊 Example Prediction

```python
example_project = [[12, 10, 250, 5, 4]]
predicted = model.predict(example_project)
print(predicted[0])  # Output: 'Medium' (for example)

🚀 Getting Started
Requirements

    Python 3.8+

    pandas

    numpy

    scikit-learn

    openpyxl (for Excel support)

Installation

pip install pandas numpy scikit-learn openpyxl

Run the script

python project_complexity_classifier.py

✅ Output

    Model evaluation using a classification report.

    Printed prediction for an example project.

    Synthetic data saved as an Excel file for exploration.

📌 Notes

    The synthetic data is generated with random but realistic values.

    The complexity scoring formula is simple and can be customized as needed.

    This is a demo project and can be extended with real project datasets.

📬 Contact me
Github: https://github.com/Otutu11
Name: Otutu Anslem


