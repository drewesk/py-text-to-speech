import streamlit as st
from gtts import gTTS
import os

# Define the prayer text
prayer_text = "Ben Pohraht Yohseff Ben Pohraht Ahlei Ahyeen -- Bahnnot Tzah-ahdah -- Ahhley Shoor."

# Always remove old file (if it exists)
if os.path.exists("prayer.mp3"):
    os.remove("prayer.mp3")

# Generate a fresh audio file
tts = gTTS(text=prayer_text, lang='en', slow=True)
tts.save("prayer.mp3")

# Streamlit UI
st.title("Evil Eye Prayer Audio")

with open("prayer.mp3", "rb") as audio_file:
    st.audio(audio_file.read(), format='audio/mp3')
