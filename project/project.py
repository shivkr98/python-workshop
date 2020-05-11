#plz read project.txt file before implimentation

import random
import pyttsx3
import speech_recognition as sr 
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am aim Sir. i am here to help you")  

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query     

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def dice_simulate():

    while(1):
        speak("hello sir, can i start")
        g =str(listen())
        if g== 'yes':
        
            number = random.randint(1,6)
            speak("your number is" + number)
            while(1):
                speak("do you want to roll dice again sir")
                flag = str(listen())
                if flag == 'yes':
                    number = random.randint(1,6)
                    speak("your number is" + number)
                elif flag == 'no':
                    speak("ending the game")
                    return
        elif g== 'yes lets start' :
            number = random.randint(1,6)
            speak("your number is" + number)
            while(1):
                speak("do you want to roll dice again sir")
                flag = str(listen())
                if flag == 'yes':
                    number = random.randint(1,6)
                    speak("your number is" + number)
                elif flag == 'no':
                    speak("ending the game")
                    return
        elif g== 'no':
            speak("ok sir, ending the game")
        else:
            speak("sorry sir can you speak again ")       

             
if __name__ == "__main__":
    
    wishMe()
    while (1):
        dice_simulate()

    
    

    
    
    
    


