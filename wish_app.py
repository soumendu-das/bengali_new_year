import streamlit as st
import google.generativeai as genai
import os
from gtts import gTTS

os.environ["GOOGLE_API_KEY"]="AIzaSyAk3XfMjeiivTSZ9MYHNMmHetTV7GR_Ar0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="Boishakhi AI bondhu",layout="centered")
st.title("বৈশাখী AI বন্ধু")
st.markdown("শুভ নববর্ষে তোমার ডিজিটাল AI বন্ধু")
st.caption("developed by SOUMENDU DAS")
name=st.text_input("enter name")
if st.button("Press button"):
     st.balloons()
     st.image("pic.jpg")
     prompt=f""" Create a warm and heartfelt Bengali New Year (Pohela Boishakh) greeting message in Bengali. The message should be personalized using the name: {name}. Clearly mention that this wish is being sent by Soumendu at the end. The tone should be festive, joyful, and respectful. Write it in beautiful Bengali script.give only ans no need to start with Here's a warm and heartfelt Pohela Boishakh greeting for , in Bengali script, signed by Soumendu:

"""
     response=model.generate_content(prompt)
     st.success(response.text);
     tts=gTTS(text=response.text,lang="bn")
     tts.save("output.mp3")
     st.audio("output.mp3");
