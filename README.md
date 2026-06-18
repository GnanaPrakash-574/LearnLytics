# 📚 Learnlytics

Learnlytics is a personalized learning analytics and quiz platform built using Python and Streamlit. It helps students assess their knowledge through quizzes, track their performance, identify strengths and weaknesses, and receive personalized study recommendations.

## 🚀 Features

### 📝 Quiz System
- Subject-wise quizzes
- Topic-wise question selection
- Difficulty levels (Easy, Medium, Hard)
- Multiple-choice questions

### 📊 Analytics Dashboard
- Overall accuracy tracking
- Subject-wise performance analysis
- Accuracy trend visualization
- Quiz history tracking

### 💡 Personalized Recommendations
- Weak subject detection
- Strong subject identification
- Difficulty recommendations
- Topic-based study suggestions

### 🔥 Study Streak Tracking
- Daily study streak monitoring
- Consistency tracking

### ⚙️ Settings
- Difficulty preferences
- Quiz history reset
- User customization options

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- JSON

---

## 📂 Project Structure

```text
Learnlytics/
│   analytics.py
│   main.py
│   quiz.py         # Original CLI
│   README.md
│   requirements.txt
│   storage.py
|
│   🏠Home.py
│   
├───data
│       performance.json
│       questions.json
│       settings.json
│       
├───pages
│       1_📝Quiz.py
│       2_📜Results.py
│       3_📊Analytics.py
│       4_💡Get Recommendations.py
│       5_⚙️Settings.py
│       
└───static
        homeimage.png
```

---

## 📈 Key Metrics Tracked

- Overall Accuracy
- Subject Accuracy
- Topic Accuracy
- Quiz Attempts
- Study Streak
- Best Subject
- Weakest Subject

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/GnanaPrakash-574/LearnLytics
cd Learnlytics
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run 🏠Home.py
```

---

## Project Evolution

> Started as a CLI-based Python quiz application.
>
> Added performance tracking and analytics.
>
> Migrated to Streamlit as a web application
>
> Implemented recommendations, study streaks and learing insights.

## 🎯 Future Improvements

- AI-powered study recommendations
- AI chatbot for doubt solving
- User authentication
- Cloud database integration
- Leaderboards and achievements
- PDF performance reports

---

## 👨‍💻 Developed By

Gnana Prakash

First-Year Computer Science Student

Learnlytics – Personalized Learning Analytics Platform

