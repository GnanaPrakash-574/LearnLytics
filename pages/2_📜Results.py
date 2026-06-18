import streamlit as st

st.set_page_config(page_title="LearnLytics",page_icon="📝",layout="wide")

if "latest_result" not in st.session_state:
    st.warning("No quiz attempted recently")
    st.stop()

result = st.session_state.latest_result
question_review = st.session_state.question_review
st.header("Results")
st.caption("Here's how you performed in your latest quiz attempt")
st.success("Quiz result saved successfully!")

col1,col2,col3,col4 = st.columns(4)
with col1:
    with st.container(border=True):
        st.metric("🏆Score",f"{result["correct"]}/{result["total_questions"]}")
with col2:
    with st.container(border=True):
        st.metric("🎯Accuracy",f"{result["accuracy"]}%")
with col3:
    with st.container(border=True):
        st.metric("✅Correct",result["correct"])
with col4:
    with st.container(border=True):
        st.metric("❌Wrong",result["wrong"])

if result["accuracy"] >= 80:
    st.balloons()
    st.success("Excellent work! Keep it up!")
elif result["accuracy"] >= 40:
    st.info("Good job! A little more practice and you'll master it!")
else:
    st.warning("Don't be discouraged! Review the material and try again!")

col1,col2= st.columns([2,1])

st.divider()
st.write("")

with col1:
    with st.container(border=True):
        st.subheader("Question Review")
        st.write("")
        
        for q in question_review[:2]:
            st.write(f"**Question:** {q['question']}")
            st.write(f"**Your Answer:** {q['user_answer']}")
            st.write(f"**Correct Answer:** {q['correct_answer']}")
                
            if q["is_correct"]:
                st.success("✅ Correct")
            else:
                st.error("❌Wrong")
            st.write("")
            st.divider()
        
        if len(question_review) > 2:
            with st.expander(f"Show {len(question_review)-2} more questions"):
                for q in question_review[2:]:
                    st.write(f"**Question:** {q['question']}")
                    st.write(f"**Your Answer:** {q['user_answer']}")
                    st.write(f"**Correct Answer:** {q['correct_answer']}")
                        
                    if q["is_correct"]:
                        st.success("✅ Correct")
                    else:
                        st.error("❌Wrong")
                    st.write("")
                    st.divider()

with col2:
    with st.container(border=True):
        st.subheader("Quiz Info")

        st.write("")
        st.write(f"📖 Subject   :   {result["subject"]}")
        st.write(f"📖 Topic     :   {result["topic"]}")
        st.write(f"📊 Difficulty : {result["difficulty"]}")
        st.write(f"📅 Date      :   {result["date"]}")
        st.write(f"❔ Total Question : {result["total_questions"]}")
