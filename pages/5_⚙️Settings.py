import streamlit as st
import json

st.set_page_config(page_title="Settings", page_icon="⚙️")

st.title("⚙️ Settings")

st.divider()

difficulty = st.selectbox("Default Difficulty",["easy", "medium", "hard"])
questions = st.slider("Questions Per Quiz",min_value=5,max_value=20,value=5)

if st.button("💾 Save Settings"):
    
    settings = {"difficulty": difficulty,"questions_per_quiz": questions}

    with open("data/settings.json", "w") as f:
        json.dump(settings, f, indent=4)
    st.success("Settings saved!")

st.divider()
st.subheader("Danger Zone")

if st.button("🗑️ Reset Quiz History"):
    with open("data/performance.json", "w") as f:
        json.dump([], f)

    st.success("Quiz history deleted!")