import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # לפני imports של llm
import os
#st.write("KEY loaded?", bool(os.getenv("OPENAI_API_KEY")))


from services.prompts import study_plan_prompt
from services.llm import generate_study_plan

st.set_page_config(page_title="AI Study Plan", layout="centered")
st.title("📚 AI Study Planner")

subject = st.text_input("What do you want to study?")
level = st.selectbox("Your level:", ["Beginner", "Intermediate", "Advanced"])
days = st.slider("How many days?", 1, 30, 7)

if st.button("Generate study plan"):
    if subject:
        with st.spinner("Creating your study plan..."):
            prompt = study_plan_prompt(subject, level, days)
            plan = generate_study_plan(prompt)
            st.success("Here is your study plan:")
            st.write(plan)
    else:
        st.warning("Please enter a subject")
