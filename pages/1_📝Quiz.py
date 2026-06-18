import streamlit as st
import storage
from datetime import datetime
import json

st.set_page_config(page_title="LearnLytics",page_icon="📝",layout="wide")

st.title("📝 Quiz")
st.write("### Test your knowledge and improve!!")

questions_df = storage.load_questions()

if questions_df.empty:
    st.error("No questions available")
    st.stop()

try:
    with open("data/settings.json", "r") as f:
        settings = json.load(f)
    default_difficulty = settings.get("difficulty", None)
    default_questions = settings.get("questions_per_quiz", 5)
except:
    default_difficulty = None
    default_questions = 5

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted= False

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        subject = st.selectbox("Subject",questions_df["subject"].unique())

with col2:
    with st.container(border=True):
        topics = list(questions_df[questions_df["subject"] == subject]["topic"].unique())
        topics.insert(0, None)
        topic = st.selectbox("Topic",topics)

with col3:
    with st.container(border=True):
        difficulty_options=[None,"easy","medium","hard"]
        difficulty= st.selectbox("Difficulty",difficulty_options,index = difficulty_options.index(default_difficulty))
       
with col4:
    with st.container(border=True):
        num_questions = st.number_input("Questions",min_value=1,max_value=20,value=default_questions)

if st.button("🚀 Start Quiz", use_container_width=True):

    filtered_questions = questions_df[questions_df["subject"] == subject]

    if topic is not None:
        filtered_questions = filtered_questions[filtered_questions["topic"] == topic]
    if difficulty is not None:
        filtered_questions = filtered_questions[filtered_questions["difficulty"] == difficulty]
    if filtered_questions.empty:
        st.error("No questions available")
        st.stop()

    if len(filtered_questions) < num_questions:
        num_questions = len(filtered_questions)

    st.session_state.quiz_questions = (filtered_questions.sample(n=num_questions).reset_index(drop=True))
    st.session_state.quiz_started = True
    st.session_state.quiz_submitted = False


if st.session_state.get("quiz_started", False):

    quiz_df = st.session_state.quiz_questions
    st.divider()
    st.subheader("Questions")

    for i, row in quiz_df.iterrows():
        st.write(f"### Q{i+1}. {row['question']}")
        st.radio("Choose Answer",row["options"],key=f"question_{i}")
        st.write("")

    submit =st.button("✅ Submit Quiz",use_container_width=True,disabled=st.session_state.quiz_submitted)

    if submit:
        correct = 0
        review=[]

        for i, row in quiz_df.iterrows():
            user_answer = st.session_state[f"question_{i}"]
            is_correct= user_answer == row["answer"]
            if is_correct:
                correct += 1
        
            review.append({"question":row["question"],
                           "user_answer":user_answer,
                           "correct_answer":row["answer"],
                           "is_correct":is_correct})
        

        total_questions = len(quiz_df)
        wrong = total_questions - correct
        accuracy = round((correct / total_questions) * 100,2)
        st.session_state.quiz_submitted = True

        st.divider()

        
        result = {"date": datetime.now().date().isoformat(),
                  "subject": subject,
                  "topic": topic,
                  "difficulty": difficulty,
                  "total_questions": total_questions,
                  "correct": correct,
                  "wrong": wrong,
                  "accuracy": accuracy}

        storage.save_performance(result)
        st.success("Quiz result saved successfully!")
        st.session_state.quiz_submitted= True
        st.session_state.quiz_started= False
        st.session_state.latest_result= result
        st.session_state.question_review= review
        
        st.switch_page("pages/2_📜Results.py")