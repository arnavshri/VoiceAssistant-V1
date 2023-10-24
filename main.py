import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_audio import *
from news import *
from jokes import *
from weather import *
import randfacts
import datetime


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice;',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

today_date=datetime.datetime.now()


r = sr.Recognizer()

speak("Hello sir, I'm JARVIS")
speak("Today is "  +today_date.strftime("%d") + "of" + today_date.strftime("%B")+ "And its Currently" + today_date.strftime("%I"))
speak("and The weather in Indore is " +str(temp()) +" Degree Celcius")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if "Jarvis" in text:
    speak("What can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text2=r.recognize_google(audio)

if "information" in text2:
    speak("You need information related to which Topic?")

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        print(infor)

        speak("searching {} in wikipedia".format(infor))
        assist = infow()
        assist.get_info(infor)

elif "play" and "video" in text2:
    speak("You want to play which video")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio = r.listen(source)
        vid = r.recognize_google(audio)

        speak("playing {} in youtube".format(vid))
        assist = music()
        assist.play(vid)

elif "news" in text2:
    speak("Sure Sir,Now I will read news for you")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" in text2:
    speak("Sure Sir")
    x=randfacts.get_fact()
    print(x)
    speak("Did you know that, " +x)

elif "joke" in text2:
    speak("Sure Sir,Now I will tell joke for you")
    arr=joke()
    print(arr[0])
    print(arr[1])
    speak(arr[0])
    speak(arr[1])

        