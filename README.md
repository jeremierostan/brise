# 🗣️Brise
_A simple speech-to-text streamlit app_
This app is part of the "5mn Series", a nano-training program by Jérémie Rostan and Pascal Vallet demonstrating the myriad ways in which AI technologies can help enhance school leadership.
In line with the SAMR model, AI integration can help school leaders be more efficient, effective, and innovative. An example would be using AI to transcribe voice recordings, then process and even share them in some way - whether it is sending high-quality feedback aligned with a school's unique philosophy after a class observation, distributing action items after a meeting, or whatever it might be.
This is the focus of Month 1, with Week 1 looking specifically at speech-to-text technologies. In this series, Jérémie and Pascal present both simple paid options, such as Audiopen, and more advanced but free open source alternatives. This is where **🗣️Brise** comes in. 

With the help of Mistral Large (https://mistral.ai/news/mistral-large/), Pyton code leveraging the Streamlit framework was used to create an app making speech-to-text a breeze (Mistral is also the name of a strong wind in Southeastern France). **🗣️Brise** records the user's voice, and uses OpenAI Whisper to transcribe it on their own computer. All data stays local. No API key is even needed. 

To run the app, simply:
1. Download and install Python on your computer (https://www.python.org/downloads/)
2. Download and install a code editor such as VS Code (https://code.visualstudio.com/)
4. Open brise.py
5. Install the necessary packages by running the following in your terminal:
```
pip install streamlit sounddevice scipy whisper numpy
```
6. Run the app with:
```
streamlit run brise.py
```
A breeze!


NB. You might need to 
- Install download and install Homebrew (https://brew.sh/)
- Then install PortAudio
```
brew install portaudio
```
- Resintall sounddevice
```
pip install sounddevice --force-reinstall
```
