import pyttsx3
print("\t\n\tEnter the text")
txt=input("\tpress enter at the end\n\t")
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',140)
engine.say(txt)
engine.runAndWait()