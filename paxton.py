from ast import Expression
from email.mime import audio
from http import server
import os
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Shakila")
        speak("Good Morning Shaakila")
    
    elif hour>=12 and hour<18:
        print("Good Afternoon Shakila")
        speak("Good Afternoon Shaakila")

    else:
        print("Good Evening Shakila")
        speak("Good Evening Shaakila")

    print("Paxton Here! How may I help you?")
    speak("Paxton Here! How may I help you?")

def takeCommand():
    #Takes: Microphone Input & Returns: String Output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.dynamic_energy_threshold = False
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-bn')
        print(f"You said: {query}\n")

    except Exception as e:
        #print(e)
        print("Would you repeat please?")
        speak("Would you repeat please?")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.cm', 587)
    server.ehlo()
    server.starttls()
    server.login('shakila.miti10@gmail.com', 'shakila1911297642')
    server.sendmail('shakila.miti10@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("Opening Youtube...")
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening goggle")
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            print("Opening StackOverflow...")
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            print("Playing your favourite music...")
            speak("playing your favourite music")
            webbrowser.open("youtube.com/watch?v=iUm1NcTsqJU&list=RDiUm1NcTsqJU&start_radio=1")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print("The time is", strTime)
            speak(f"The time is {strTime}")

        elif 'stupid' in query:
            print("That's Offensive!!")
            speak("that's offensive!")
        
        elif 'open vs code' in query:
            print("Opening...")
            speak("Opening")
            codePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email my friend' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "zihadislam3555@gmail.com"
                print("Email has been sent successfully!")
                speak("email has been sent successfully!")
            
            except Exception as e:
                print(e)
                print("Sorry Shakila. I couldn't send the email 😞")
                speak("Sorry Shakila. I couldn't send the email")

        elif 'open notepad' in query:
            print("Opening...")
            speak("Opening")
            codePath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(codePath)
        
        elif 'how are you' in query:
            print("I'm doing just fine. How may I help you?")
            speak("I'm doing just fine. How may I help you?")
        
