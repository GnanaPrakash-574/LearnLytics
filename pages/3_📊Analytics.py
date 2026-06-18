import streamlit as st
import pandas as pd
import analytics
import storage

st.set_page_config(page_title="Learnlytics",page_icon="🧠",layout = "wide")

performance = storage.load_performance()

if performance.empty:
    st.warning("No quiz history found. Complete a quiz first to get Analytics.")
    st.stop()
st.title("Analytics")
st.write("### Visualize your learning performance")
st.write("")


col1,col2,col3,col4= st.columns(4)
with col1:
    with st.container(border=True):
        performance = storage.load_performance()
        st.metric("📝 Quizzes Taken",len(performance))
with col2:
        with st.container(border=True):
            st.metric("🎯 Avg Accuracy",round(analytics.overall_stats()[3],2))
with col3:
        with st.container(border=True):
            st.metric("🏆 Strong Subject",analytics.best_subject()[0])
with col4:
        with st.container(border=True):
            st.metric("⚠️ Weakest Subject",analytics.weak_subject()[0])

st.divider()

with col1:
    with st.container(border=True):
         st.metric("🔥Study Streak",analytics.study_streak())
with col2:
    with st.container(border=True):
        performance =  storage.load_performance()
        if performance.empty:
            st.metric("❔Questions Solved",0)
        else:
            questions = performance["total_questions"].sum()
            st.metric("❔Questions Solved",questions)
with col3:
    with st.container(border=True):
        performance =  storage.load_performance()
        if performance.empty:
            st.metric("📈Correct Answers",0)
        else:
            correct = performance["correct"].sum()
            st.metric("📈Correct Answers",correct)
with col4:
    with st.container(border=True):
         performance =  storage.load_performance()
         if performance.empty:
             st.metric("📉Wrong Answers",0)
         else:
            wrong = performance["wrong"].sum()
            st.metric("📉Wrong Answers",wrong)

col1,col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Accuracy Trend")
        trend = analytics.overall_accuracy_trend()
        if trend is not None:
            st.line_chart(trend)
        
with col2:
     with st.container(border=True):
          st.subheader("Accuracy by Subject")
          accuracy = analytics.all_subjects_performance()
          if accuracy is not None:
               st.bar_chart(accuracy)
          else:
              st.divider()
              st.write("Attempt a subject for Accuracy Analysis")

with col1:
    with st.container(border=True):
        st.subheader("Topic Strength Analysis")
        co1,co2 = st.columns(2)

        with co1:
             st.success("Strong Topics 💪")
             strong_topics = analytics.topics_strenght("strong")
             if strong_topics is not None:
                 for topic in strong_topics.index:   
                    st.success(topic)
             if strong_topics is None:
                 st.info("No strong topics identified yet")

        with co2:
             st.error("Weak Topics ⚠️")
             weak_topics = analytics.topics_strenght("weak")
             if weak_topics is not None:
                 for topic in weak_topics.index:   
                    st.error(topic)
             if weak_topics is None:
                 st.info("No weak topics identified yet")



with st.container(border=True):
    st.subheader("Quiz History")
    data = storage.load_performance()
    if data is not None:
        st.write(data)
    