import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir . Please tell me how i may help you")
def takeCommand():
    # it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query ,"\n")
    except Exception as e :
        # print(e)
        print("say that again please..")
        return "None"
    return query
if __name__ == '__main__':

    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
         #logic
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube ' in query:
            webbrowser.open("youtube.com")

        elif 'open google ' in query:
            webbrowser.open("google.com")

        elif 'open facebook ' in query:
            webbrowser.open("facebook.com")

        elif 'open music ' in query:
            music_dir='E\\King'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs))
        elif'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir the time is {strTime}")
        elif 'open pycharm' in query:
            codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.1\\bin\\pycharm64.exe"
            speak("opening pycharm" )
            os.startfile(codepath)

        # elif 'email to fahad' in query:
        #     try:
        #         speak("what should i say?")
        #         content = takeCommand()
        #         to = ""
