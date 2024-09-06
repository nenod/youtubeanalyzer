import streamlit as st
import os
import textwrap
import requests
from io import BytesIO
from PIL import Image
from pytube import YouTube
import create_vector_db as mydb
import openai_analyzer as analyzer

video_url="https://www.youtube.com/watch?v=I4mFqyqFkxg"
video_id=""

st.set_page_config(layout="wide")
st.title("Youtube Video Summarizer")
st.write("Please enter a Youtube video URI and I will summarize it for you.")

st.cache_data.clear()

col1, col2 = st.columns([1, 1])

def analyze_video():
    #Column 1
    with col1:
        # Extract the YouTube video ID from the URL
        video_id = YouTube(video_url).video_id
        # Construct the URL of the thumbnail image
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

        #Download the thumbnail image and convert it to a PIL Image Object
        response = requests.get(thumbnail_url)
        img = Image.open(BytesIO(response.content))

        # Display the thumbnail image in Streamlit
        st.image(img)
    
    # Column 2
    with col2:
        with st.spinner("Reading Video contents ..."):
            mydb.create_db(video_url)
        
        with st.spinner("Analysis in progress: Please wait ..."):
            query = "Summarize the content and give me a brief summary."
            reponse = analyzer.get_analysis(query)

            st.subheader("Brief Summary")
            st.write(textwrap.fill(response, width=50))



with col1:
    video_url = st.text_input("YouTube Video URL", value=video_url)
    button_disabled = len(video_url.strip()) == 0
    submit_button = st.button("Submit", on_click=analyze_video, disabled=button_disabled)