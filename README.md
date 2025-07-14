# Covid-Symptom-Checker

A simple Python program that allows users to create an account and check for COVID-related symptoms. The application validates usernames and passwords and provides health recommendations based on user-reported symptoms.

---

## 📂 Project Structure

symptom-checker/
│
├── main.py         # Main script: user account creation and symptom checking
├── test.py         # Standalone script to test symptom input logic
└── README.md       # Project overview, instructions, and usage

---

## 🚀 Features

- **User Registration**:
  - Username must be at least 8 characters and include an uppercase letter.
  - Password must be at least 12 characters, include an uppercase letter and a special character.

- **Symptom Checker**:
  - Users choose symptoms from a list (1–4).
  - Based on the input, the program recommends testing, seeing a doctor, or confirms the user is COVID-free.

---
💡 Sample Output

Hello! Welcome to the COVID Symptom Checker 🩺
Please fill out the information below to create an account.

First Name: John
Last Name: Doe
Age: 30

Please enter a username: JohnD2024
Welcome, JohnD2024! Your username is valid.

Please enter a password: StrongPass!2024
Your password is valid.

Please select your symptoms:
1. Muscle aches, headaches, loss of appetite...
...
Enter your choice (1–4): 2
Recommendation: Please go home and take a test.

