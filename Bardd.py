from Bard import Chatbot
import speech_recognition as sr
import warnings
import sys
import pyttsx3

 
token = "WgjiS9twmtOcFRzPCLbRBY__aUuCGW3CT2l3WJsoejrA7_vCtjlFY3FlmvRGqXktbSBVDQ."

chatbot = Chatbot(token)

r = sr.Recognizer()

# Initialize pyttsx3
engine = pyttsx3.init() 
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')

engine.setProperty('rate', rate-45) 
engine.setProperty('voice', voices[1].id)

def prompt_bard(prompt):
    response = chatbot.ask(prompt)
    return response['content']

def speak(text):
   
    cleaned_text = text.replace('*', '')

    engine = pyttsx3.init()
    engine.say(cleaned_text)
    engine.runAndWait()
    
speak("Hello There , I'm bard, Teena's Boy Friend...")
speak("How can i help you ")

def main():
    while True:
        try:
            print("Listening.....")
           
            with sr.Microphone() as source:
                audio = r.listen(source)
           
            prompt_text = r.recognize_google(audio, language='en-in')
            prompt_text = prompt_text.strip()
            print("Recognizing.....", prompt_text, '\n')
           
            if len(prompt_text) == 0:
                print("Pardon.......")
                continue
        except Exception as e:
            print("Error transcribing audio: ", e)
            continue
    
        response = prompt_bard(prompt_text)
     
        print("Bard's response:", response, '\n')
       
        speak(response)

main()
