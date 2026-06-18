import streamlit as st
import analytics
import storage

st.set_page_config(page_title="Recommendations",page_icon="💡",layout="wide")

st.title("💡 Personalized Recommendations")
st.write("Based on your quiz performance, here are your personalized study recommendations.")

performance = storage.load_performance()

if performance.empty:
    st.warning("No quiz history found. Complete a quiz first to get recommendations.")
    st.stop()

st.divider()

weak_subject = analytics.weak_subject()
best_subject = analytics.best_subject()

weak_topics = analytics.topics_strenght("weak")
strong_topics = analytics.topics_strenght("strong")

streak = analytics.study_streak()

recommended_level = None

if weak_subject is not None:
    recommended_level = analytics.recommended_difficulty(weak_subject[0])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🔥 Study Streak",streak)

with col2:
    if weak_subject:
        st.metric("⚠ Weak Subject",weak_subject[0])

with col3:
    if best_subject:
        st.metric("🏆 Best Subject",best_subject[0])

st.divider()

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("📌 What You Should Focus On")
        if weak_subject:
            accuracy = round(weak_subject[1], 2)
            if accuracy < 40:
                st.error("🚨 High Priority Subject")
            elif accuracy < 60:
                st.warning("⚠ Medium Priority Subject")
            else:
                st.success("✅ Good Progress")
            st.warning(
                f"Your weakest subject is **{weak_subject[0].title()}** " f"with an average accuracy of **{accuracy}%**.")

        if recommended_level:
            st.info(f"Recommended next quiz: **{weak_subject[0].title()} - {recommended_level.title()} Difficulty**")

        st.write("### 🔴 Weak Topics")

        if weak_topics is None:
            st.success("No weak topics identified yet.")
        else:
            for topic, score in weak_topics.items():
                st.write(f"🔴 {topic.title()} — {round(score,2)}%")

with col2:
    with st.container(border=True):
        st.subheader("💪 Your Strengths")
        if best_subject:
            st.success(f"Best performing subject: **{best_subject[0].title()}** "f"({round(best_subject[1],2)}%)")

        st.write("### 🟢 Strong Topics")

        if strong_topics is None:
            st.info("No strong topics identified yet.")
        else:
            for topic, score in strong_topics.items():
                st.write(f"🟢 {topic.title()} — {round(score,2)}%")

st.divider() 

with st.container(border=True):
    st.subheader("📚 Suggested Study Plan")
    if weak_subject:
        st.markdown(f"""
### Recommended Actions
1. Spend extra study time on **{weak_subject[0].title()}**
2. Practice quizzes at **{recommended_level.title()}** difficulty
3. Review weak topics before attempting harder quizzes
4. Take quizzes daily to improve your study streak
5. Revisit incorrect answers from previous quizzes
6. Track your progress using the Analytics page

### Current Focus
🎯 Subject: **{weak_subject[0].title()}**
🎯 Difficulty: **{recommended_level.title()}** """)

st.success("🚀 Keep practicing consistently. Small improvements every day lead to big results!")