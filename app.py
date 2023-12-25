import streamlit as st
import os
from pytube import YouTube
from bs4 import BeautifulSoup
from moviepy.editor import VideoFileClip
import whisper
import argostranslate.package
import argostranslate.translate
import torch

st.title("YouTube Video Translator")
form = st.form("input URL")
url = form.text_input('YouTube Video URL:',value='',placeholder='Paste your video URL here')
selected_language = st.selectbox("Select your desired language:", ["Arabic", "Chinese", "French", "German", "Hindi", "Italian", "Japanese", "Polish", "Russian", "Spanish"])
to_code = ''
if selected_language == "Arabic":
    to_code = "ar"
elif selected_language == "Chinese":
    to_code = "zh"
elif selected_language == "French":
    to_code = "fr"
elif selected_language == "German":
    to_code = "de"
elif selected_language == "Hindi":
    to_code = "hi"
elif selected_language == "Italian":
    to_code = "it"
elif selected_language == "Japanese":
    to_code = "ja"
elif selected_language == "Polish":
    to_code = "pl"
elif selected_language == "Russian":
    to_code = "ru"
elif selected_language == "Spanish":
    to_code = "es"

form.form_submit_button("Proceed")


def get_videotext(url, to_code):
    print("to_Code: ", to_code)
    download_dir_video = "downloaded_videos"
    os.makedirs(download_dir_video, exist_ok=True)
    download_dir_captions = "downloaded_captions"
    os.makedirs(download_dir_captions, exist_ok=True)
    yt = YouTube(url)
    video = yt.streams.filter(file_extension='mp4').first()
    print("yt: ", yt.streams.first())
    video.download(output_path=download_dir_video)
    #get audio
    audio_dir = "audio"
    os.makedirs(audio_dir, exist_ok=True)

    video_filename = os.listdir(download_dir_video)[0]
    audio_file_name = os.path.splitext(video_filename)[0]
    video_file_path = os.path.join(download_dir_video, video_filename)
    audio_file_path = os.path.join(audio_dir, f"{audio_file_name}.wav")

    video = VideoFileClip(video_file_path)
    video.audio.write_audiofile(audio_file_path)

    ##audio to text
    model = whisper.load_model("base")

    result = model.transcribe(os.path.join(audio_dir, f"{audio_file_name}.wav"))
    segments = result.get("segments", [])

    time_results = []
    text_results = []

    for segment in segments:
        start_time_sec = segment.get("start", 0.0)
        start_time_formatted = "{:02d}:{:02d}:{:06.3f}".format(
            int(start_time_sec // 3600),
            int((start_time_sec % 3600) // 60),
            start_time_sec % 60
        )
        time_results.append(start_time_formatted)
        text_results.append(segment.get("text", "").strip())

    from_code = "en"
    # to_code = "fr"

    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

    translated_text_results = [argostranslate.translate.translate(text, from_code, to_code) for text in text_results]


    return time_results, text_results, translated_text_results

print(url)
column_width = 100
with st.spinner(f'Please wait while we create translations in {selected_language}...'):
    if url:
        time_results, text_results, translated_text_results= get_videotext(url, to_code)

        table_style = """
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                    color: black;
                }
            </style>
        """


        table_header = "<tr><th>TimeStamp</th><th>Original</th><th>Translated</th></tr>"

        table_rows = "".join(f"<tr><td>{time}</td><td>{text}</td><td>{translated_text}</td></tr>"
                             for time, text, translated_text in zip(time_results, text_results, translated_text_results))

        table_html = f"<table>{table_header}{table_rows}</table>"


        st.write(table_style, unsafe_allow_html=True)
        st.write(table_html, unsafe_allow_html=True)