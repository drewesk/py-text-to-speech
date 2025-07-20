import streamlit as st
from gtts import gTTS
import os
import uuid

st.set_page_config(page_title="Text-to-Speech", layout="centered")
st.title("🗣️ Speak Any Text")

# Input box
user_text = st.text_area("Enter any text to read aloud:", height=200)

if st.button("🔊 Generate Speech"):
    if user_text.strip():
        # Generate unique filename each time
        filename = f"{uuid.uuid4().hex}.mp3"

        # Convert text to speech
        tts = gTTS(text=user_text, lang='en', slow=True)
        tts.save(filename)

        # Play audio
        with open(filename, "rb") as f:
            st.audio(f.read(), format="audio/mp3")

        # Clean up after playback (optional)
        os.remove(filename)
    else:
        st.warning("Please enter some text first.")
