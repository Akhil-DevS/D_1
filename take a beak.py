import time
import pyttsx3
from plyer import notification

def speak(self, audio):
    engine=pyttsx3.init('sapi5')
    voice=engine.getProperty('voices')
    engine.setProperty('voices',voice[1].id)
    engine.say(audio)
    engine.runAndWait()

def take_break():
    speak("shall we start?")
    ans=input('\n(y/n)')


take_break()