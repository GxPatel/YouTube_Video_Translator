# NJIT: Intro to AI project

- The "YouTube Video Translator" project is a tool designed to take a YouTube video link and translate its captions into 10 different languages chosen by the user. It displays the translated output in three columns: the time stamps, the original captions, and the corresponding translated captions. This project utilizes AI to facilitate multilingual accessibility and understanding of video content, enabling users to experience videos in their preferred languages.


## Specifications:
### Milestone 1 (Source Videos and Closed Captions): 
- Creates a python API that will download the video and its closed captions from youtube.

### Milestone 2 (Speech to Text): 
- Creates a Python API that will separate the audio from the video and convert it to text. For this you will use libraries such as 'whisper'.

### Milestone 3 (Source Text to Target Text): 
- Creates a Python API that will translate the text from English to a language of your choosing. For this, I specifically used a pretained model from HuggingFace.

### Milestone 4 (Target Text to Speech): 
- Creates a Python API that will convert the translated text to speech using a pretrained HuggingFace model also.

### Milestone 5 (Stitching it all together): 
- Build a UI in Hugging Face Spaces and Streamlit Spaces that will accept as input a youtube video and will output the video with subtitles to a language of your choosing.

### You can run the application using following command in your python interpretor:
- "streamlit run app.py"


![ss0](https://github.com/GxPatel/YouTube_Video_Translator/assets/105250604/ac2d6366-5ce1-49bf-87ce-00f986d52434)
![ss1](https://github.com/GxPatel/YouTube_Video_Translator/assets/105250604/56942922-62bd-4b68-bc79-042994ce8bfd)
![ss3](https://github.com/GxPatel/YouTube_Video_Translator/assets/105250604/66aee03f-c36e-426c-b5dd-de119d6335fc)
