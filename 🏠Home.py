import streamlit as st
import quiz
import analytics
import storage
import os

st.set_page_config(page_title="Learnlytics",page_icon="🧠",layout = "wide")

col1,col2 = st.columns([2,1])

with col1:
    st.markdown("### Welcome to")
    st.markdown("# 📚 LearnLytics")
    st.write("")
    st.markdown("#### Smart Quiz & Performance Analytics Platform")
    st.write("")
    st.write("Track Your Performance, Ideantify Weak topics" \
    " And Improve Your Learning Smarter Everyday")


with col2:
    st.image(os.path.join(os.getcwd(),"static","homeimage.png"),width=400)

st.write("")
st.write("")
st.divider()
st.header("🚀 Features")
col1,col2,col3,col4= st.columns(4)

with col1:
    with st.container(border = True):
        st.subheader("📝 Take Quiz")
        st.write("Practice with topic-wise quizzes")

        if st.button("Go to Quiz➡️"):
            st.switch_page("pages/1_📝Quiz.py")

with col2:
    with st.container(border = True):
        st.subheader("📊 View Analytics")
        st.write("Analyze your performance with charts")

        if st.button("view Analytics➡️"):
            st.switch_page("pages/3_📊Analytics.py")


with col3:
    with st.container(border = True):
        st.subheader("📜 Track Results")
        st.write("See your progress and accuracy")

        if st.button("Track Results➡️"):
            st.switch_page("pages/2_📜Results.py")

with col4:
    with st.container(border = True):
        st.subheader("💡 Recommendations")
        st.write("Personalized study suggestions")

        if st.button("Get Recommendations➡️"):
            st.switch_page("pages/4_💡Get Recommendations.py")

st.write("")
st.divider()

st.header("🔍 Quick Overview")
st.write("")

with st.container(border = True):
    col1,col2,col3,col4= st.columns(4)

    with col1:
        performance = storage.load_performance()
        st.metric("📝 Quizzes Taken",len(performance))
    with col2:
        st.metric("🎯 Avg Accuracy",round(analytics.overall_stats()[3],2))
    with col3:
        st.metric("🏆 Strong Subject",analytics.best_subject()[0])
    with col4:
        st.metric("⚠️ Weakest Subject",analytics.weak_subject()[0])