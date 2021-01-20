
from time import ctime
import webbrowser
import time
import datetime
import playsound
import os
import random
import pyjokes
from gtts import gTTS
import speech_recognition as sr
r=sr.Recognizer()

def recod_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio=r.listen(source)
        voice_data=''
    

        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak('say something')
        except sr.RequestError:
            alexis_speak('sorry, my speech service is down')
        return voice_data

def jokes():
    alexis_speak(pyjokes.get_joke())

def alexis_speak(audio_string):
    tts=gTTS(text=audio_string, lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-'+ str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('my name is pritam')
    elif 'what time is it' in voice_data:
        alexis_speak(ctime())
    elif 'search' in voice_data:
        search=recod_audio('what do u want to search for?')
        url='https://google.com/search?q='+ search
        webbrowser.get().open(url)
        alexis_speak('here what i found for'+search)
    elif 'find location' in voice_data:
        location=recod_audio('what is the location?')
        url='https://google.nl/maps/place/'+ location+ '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('here is the location of'+location)
    elif 'play songs' in voice_data:
        songs_dir = 'C:\\Users\\pritamsing\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs'
        songs =os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir,songs[0]))
    elif 'remember' in voice_data:
        data=recod_audio('what should i remember')
        alexis_speak('you said me to remember tht'+data)
        remember=open('data.txt','w')
        remember.write(data)
        remember.close()
    elif 'joke' in voice_data:
        jokes()
    elif 'logout' in voice_data:
        os.system('shutdown -1')
    elif 'shutdown' in voice_data:
        os.system('shutdown /s /t 1')
    elif 'restart' in voice_data:
        os.system('shutdown /r /t 1')  
    elif 'exit' in voice_data:
        exit()

def wishme():
    alexis_speak("welcome back sir")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour <=12:
        alexis_speak("good morning sir")
    elif hour>=12 and hour <18:
        alexis_speak("good afternoon sir")
    elif hour >=18 and hour <24:
        alexis_speak("good evening sir")
    else:
        alexis_speak("good night sir")
    alexis_speak("jarvis at your service.")
wishme()

time.sleep(1)
alexis_speak('how can i help you?')
while 1:
    voice_data=recod_audio()
    respond(voice_data)




    

