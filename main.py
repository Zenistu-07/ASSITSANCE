import pyttsx3 
import datetime
import subprocess

import webbrowser
import time
import os
from PyDictionary import PyDictionary
from difflib import get_close_matches

import wikipedia
from Bard import Chatbot
import pywhatkit

import pyaudio
import openai

import speech_recognition as sr
import requests
import random
import pyautogui



token = "WgjiS9twmtOcFRzPCLbRBY__aUuCGW3CT2l3WJsoejrA7_vCtjlFY3FlmvRGqXktbSBVDQ."

engine = pyttsx3.init('sapi5')



voices = engine.getProperty('voices')



engine.setProperty('voice', voices[2].id)



engine.setProperty('rate', 180)

now = datetime.datetime.now()

    
def wishme():

    if now.time() < datetime.time(12,0):
        print("Good Morning")
        speak(now.time)

        engine.say("Good Morning ")

        engine.runAndWait()

    elif now.time() < datetime.time(18,0):
        print("Good Afternoon")

        engine.say("Good afternoon ")
        
        engine.runAndWait()
    else:
        print("Good Evening")
        engine.say("good evening ")

        engine.runAndWait()


jio = {
        "country": "in",
        "apiKey": "your-api-key" 
    }
def get_news_headlines():
    url = "https://newsapi.org/v2/top-headlines"
    response = requests.get("https://newsapi.org/v2/top-headlines", params=jio)
    if response.status_code == 200:
        data = response.json()
        headlines = [article['title'] for article in data['articles']]
        return headlines
    else:
        print("Error fetching news headlines")
        return []
news_headlines = get_news_headlines()


def handle_response(response_text):
    speak(response_text)



   
chatStr = ""

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    
    if query is None or query.strip() == "":
        return None
    
    openai.api_key = "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"
    chatStr += f": {query}\n"
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    ai_response = response["choices"][0]["text"]
    question_types = ["what", "when", "where", "who", "why", "how","can","is","do"]
    question = query.strip().lower()
    if any(question.startswith(q) for q in question_types):
        handle_response(ai_response)
    else:
        return None




def Cal_day():
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
        
        return day_of_the_week
    
    
def shedule():
        day = Cal_day().lower()
        speak("today's shedule is")
        Week = {"monday" : "Add your schedule",
        "tuesday" : "Add your schedule",
        "wednesday" : "Add your schedule",
        "thrusday" : "1- 2 : lunch break",
        "friday" : "Add your schedule",
        "saturday" : "Add your schedule",
        "sunday":"Add your schedule"}
        if day in Week.keys():
            speak(Week[day])


def speak(audio):
    engine.say(audio)

    engine.runAndWait()



time.sleep(1)

def take_user_input():
    user_input = input("Please enter your input: ")
    return user_input

def self():


    speak("i'm Teena")

    speak("How can i assist you today")


def prompt_bard(prompt):
    response = chatbot.ask(prompt)
    return response['content']

    

def social():
        print(command)
        if 'facebook' in command:
            speak('opening your facebook')
            webbrowser.open('https://www.facebook.com/')
        elif 'whatsapp' in command:
            speak('opening your whatsapp')
            webbrowser.open('https://web.whatsapp.com/')
        elif 'instagram' in command:
            speak('opening your instagram')
            webbrowser.open('https://www.instagram.com/')
        elif 'twitter' in command:
            speak('opening your twitter')
            webbrowser.open('https://twitter.com/Suj8_116')
        elif 'discord' in command:
            speak('opening your discord')
            webbrowser.open('https://discord.com/channels/@me')
        else :
            self.No_result_found()
            
            

def run_bradd():
    try:
        subprocess.run(['python', 'Bardd.py'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error running Bardd.py:", e)

def get_definition(word):
    # get the definition of the word
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    data = response.json()

    if not data:
        return speak("Sorry, we couldn't find a definition for that word.")
    
    elif word_index < len(words):
        word = words[word_index]
    # rest of the code for getting definition
    else:
        print("Word index out of range!")
    try:
        # get the noun definition
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
    except (KeyError, IndexError):
        return "Sorry, we couldn't find a noun definition for that word."

    return definition




def play_song(song_name):

    pywhatkit.playonyt(song_name.replace("play", ""))
    



def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = f"{data['content']} - {data['author']}"
        return quote
    else:
        print("Error fetching quote")
        return ""

def get_trending_movies():
    trending_movies = []
    api_key = "e33af6495cd02e451c5f12adf80f0f27"
    url = "https://api.themoviedb.org/3/trending/movie/day?api_key={}".format(api_key)
    res = requests.get(url).json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)
    
def translate():
    word = word.lower()
    if word in data:
        speak(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        x = get_close_matches(word, data.keys())[0]
        speak('Did you mean ' + x +
              ' instead,  respond with Yes or No.')
        ans = command().lower()
        if 'yes' in ans:
            speak(data[x])
        elif 'no' in ans:
            speak("Word doesn't exist. Please make sure you spelled it correctly.")
        else:
            speak("We didn't understand your entry.")
        return query

data = {
    'apple': 'a round fruit with red or green skin and a white inside',
    'banana': 'a long curved fruit with yellow skin and soft sweet flesh',
    'carrot': 'a long thin orange vegetable that grows underground',
    'dog': 'a domesticated mammal and common household pet',
    'elephant': 'a large gray mammal with a long trunk and ivory tusks',
    'frog': 'a cold-blooded amphibian with a smooth moist skin and long hind legs',
    'giraffe': 'a tall mammal with a long neck and spots on its coat',
    'hamburger': 'a type of sandwich made with a beef patty and various toppings',
    'iguana': 'a type of lizard with a long tail and spiny scales',
    'jacket': 'a piece of clothing worn over the upper body',
    'kangaroo': 'a marsupial with powerful hind legs for jumping and a pouch for carrying its young',
    'lemon': 'a citrus fruit with a yellow rind and sour juice',
    'monkey': 'a primate with a long tail and opposable thumbs',
    'nutmeg': 'a spice made from the seed of an evergreen tree',
    'ostrich': 'a large flightless bird with long legs and a long neck',
    'penguin': 'a flightless bird that lives in cold climates and has black and white feathers',
    'quinoa': 'a grain-like crop that is high in protein and gluten-free',
    'rhinoceros': 'a large mammal with thick skin and one or two horns on its nose',
    'strawberry': 'a sweet red fruit with small seeds on its surface',
    'tomato': 'a red or yellow fruit with a juicy pulp, commonly used in cooking',
    'umbrella': 'a device used to protect against rain or sun',
    'violin': 'a musical instrument with four strings and a bow',
    'watermelon': 'a large sweet fruit with a green rind and red pulp',
    'xylophone': 'a musical instrument with wooden bars that are struck with mallets',
    'yogurt': 'a dairy product made from fermented milk',
    'zebra': 'a striped African mammal with black and white fur',
    'abacus': 'a device used for counting and calculating',
    'butterfly': 'an insect with large colorful wings and a thin body',
    'chimpanzee': 'a primate native to Africa with a highly developed brain',
    'dolphin': 'a highly intelligent marine mammal that breathes air through a blowhole',
    'elephant': 'a large gray mammal with a long trunk and ivory tusks',
    'flamingo': 'a large wading bird with pink or orange feathers and long legs',
    'giraffe': 'a tall mammal with a long neck and spots on its coat',
    'hedgehog': 'a small spiny mammal with short legs and a pointed snout',
    'iguana': 'a type of lizard with a long tail and spiny scales',
    'jellyfish': 'a gelatinous marine creature with long trailing tentacles',
    'kangaroo': 'a marsupial with powerful hind legs for jumping and a pouch for carrying its young',
    'lemur': 'a primate native to Madagascar with a long tail and large eyes',
    'mongoose': 'a small carnivorous mammal that feeds on insects and small animals',
    'narwhal': 'a medium-sized toothed whale with a long spiral tusk',
    'octopus': 'a marine animal with eight arms and a soft body',
    'penguin': 'a flightless bird that lives in cold climates and has black and white feathers',
    'quokka': 'a small marsupial with a short tail and friendly demeanor',
    'rhinoceros': 'a large mammal with thick skin and one or two horns on its nose',
    'salamander': 'a small amphibian with a long tail and moist skin',
    'toucan': 'a brightly colored bird with a large beak',
    'urchin': 'a spiny marine animal with a round shell',
    'vulture': 'a large bird of prey that feeds on carrion',
    'walrus': 'a large marine mammal with long tusks and a thick layer of blubber',
    'xenopus': 'a genus of aquatic frogs native to sub-Saharan Africa',
    'yak': 'a large long-haired mammal with curved horns, native to the Himalayas',
    'zebra': 'a striped African mammal with black and white fur',
    'atom': 'the basic unit of a chemical element',
    'biology': 'the study of living organisms',
    'chemistry': 'the scientific study of the properties and behavior of matter',
    'DNA': 'a self-replicating material present in nearly all living organisms',
    'evolution': 'the process by which different kinds of living organisms are thought to have developed',
    'force': 'an influence that changes the motion of an object',
    'gene': 'a sequence of DNA that codes for a particular protein',
    'hypothesis': 'a proposed explanation for a phenomenon',
    'inertia': 'the tendency of an object to remain at rest or in motion in a straight line',
    'joule': 'the unit of measurement for energy',
    'kinematics': 'the study of motion without considering its causes',
    'laser': 'a device that emits light through a process of optical amplification',
    'molecule': 'a group of atoms bonded together',
    'neutron': 'a subatomic particle with no electric charge',
    'organic': 'relating to or derived from living matter',
    'photosynthesis': 'the process by which green plants and some other organisms use sunlight to synthesize foods',
    'quantum': 'the smallest amount of energy that can be gained or lost in an interaction',
    'relativity': 'the concept that there is no absolute motion or absolute rest',
    'subatomic': 'relating to particles smaller than atoms',
    'theory': 'a well-substantiated explanation of some aspect of the natural world',
    'universe': 'all existing matter and space considered as a whole',
    'velocity': 'the rate of change of displacement with respect to time',
    'work': 'the transfer of energy from one object to another through a force applied over a distance',
    'x-ray': 'a form of electromagnetic radiation used in medical imaging',
    'yield': 'the amount of product obtained in a chemical reaction',
    'zinc': 'a chemical element with the symbol Zn and atomic number 30',
    'algorithm': 'a step-by-step procedure for solving a problem or achieving a goal',
    'bug': 'an error or flaw in a program that causes it to produce unexpected or incorrect results',
    'code': 'a set of instructions that a computer can execute',
    'debugging': 'the process of finding and fixing bugs in a program',
    'function': 'a self-contained block of code that performs a specific task',
    'GUI': 'Graphical User Interface, a type of interface that allows users to interact with a program using visual elements such as buttons and menus',
    'IDE': 'Integrated Development Environment, a software application that provides comprehensive facilities to computer programmers for software development',
    'JSON': 'JavaScript Object Notation, a lightweight data interchange format',
    'loop': 'a sequence of instructions that is continually repeated until a certain condition is met',
    'method': 'a function that is associated with an object and can access the object’s data',
    'object': 'a data structure that contains data and code to manipulate that data',
    'program': 'a set of instructions that a computer can execute',
    'query': 'a request for information from a database',
    'recursion': 'a process in which a function calls itself as a subroutine',
    'source code': 'the human-readable instructions that a programmer writes to create a program',
    'syntax': 'the rules that govern the structure of programming languages',
    'variable': 'a named value that can be assigned a new value as the program runs',
    'web development': 'the process of creating websites and web applications',
    'XML': 'Extensible Markup Language, a markup language for documents containing structured information',
}

def command():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening..........")
    
        r.pause_threshold =  1.0

        audio = r.listen(source)

    try:

        print("Recognizing......")

        query = r.recognize_google(audio,language='en-in')

        print(f"You Said:{query}\n")
        
    except Exception as e:

        print(" pardon ..........")
        return "none"

    return query




    
    
    



if __name__ == "__main__":

    wishme()
    
    self()
    

    while True:

        query = command().lower()


        if 'wikipedia' in query:

            speak('searching wikipedia.....')

            query = query.replace("wikipeda....","")

            result = wikipedia.summary(query,sentences = 2)
            print(result)

            speak(result)
        elif 'tina' in query or 'teena' in query:
            speak("Yes")
        
        
        elif 'open youtube' in query:

            speak("opening youtube.......")

            webbrowser.open("youtube.com")

        if 'play' in query:

            song_name = query.replace("play music","").strip()

            speak(f"Playing {song_name} on YouTube")

            play_song(song_name)
            
        
            

        elif 'stop' in query:

            speak("ok stoping the program")
            

            break
       
        elif 'open google' in query:

            speak("opening google......")

            webbrowser.open('google.com')

        elif 'open spotify' in query:

            speak("opening spotify......")
            os.system("start spotify")

        elif 'date' in query:

            speak("today the date is.......")

            engine.say(now.strftime("%A,%B,%d,%Y"))

            engine.runAndWait()

        elif 'i love you' in query:

            speak("i love you too babe")
            
            
       # elif 'screenshot' or 'screen' or 'shot' in query:
            scshot()

        elif 'open code' in query:

            code = "C:\\Users\\codex\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(code)

        elif 'hello' in query:

            speak("Hii  sir")

        elif 'who are you' in query:

            speak("i'm a virtual assistance made by Taju")

        elif 'what are your specifications' in query:

            speak("i can perform simple task's like playing music,opening spotify and so on")
            
        elif 'college' in query:
            speak("That is RVR & JC college of engineering")

        elif 'what is your name' in query:

            speak("i'm Teena")
        
        elif 'hook up' in query:
            speak('Sorry not intrested, I am having headache, we will catch up some other time')

        elif 'what is your relationship with taju' in query:

            speak("I am his Assistance")

        elif 'open bluestacks folders' in query:

            cod = "C:\\Program Files\\BlueStacks_nxt"
            os.startfile(cod)
        elif 'internet speed' in query:
            InternetSpeed(self)
            
        elif 'movie rules' in query:

            speak("opening movierulz website")

            webbrowser.open('https://5movierulz.li/')

        elif 'open chat GPT' in query:

            speak("opening chat GPT")

            webbrowser.open('https://chat.openai.com/')
        elif 'chrome' in query:
            speak("Opening chrome")
            cc = "C:\Program Files\Google\Chrome\Application.exe"
            os.startfile(cc)
        
        
        elif 'moon' in query:
            speak("I love you")
        elif 'shop' in query:
            use = speak("what do want to shop")
            l = command()
            if 'clothes' in l or 'dress' in l or 'sarees' in l or 'shirts' in l or 'festivaloffer' in l or 'hoodies' in l:
                webbrowser.open('https://www.flipkart.com/')
            elif'laptops' in l or 'fridges' in l or 'electronics' in l or 'machines' in l:
                webbrowser.open('https://www.amazon.in/')
            else:
                speak("SOrry......404 error")
        

        elif 'instagram' in query:
            speak("opening instagram")
            webbrowser.open('https://www.instagram.com/')
        elif 'whatsapp' in query:
            speak("opening whatsapp")
            url = "https://web.whatsapp.com/"
            webbrowser.open(url)

           

       
        elif 'who' in query:
            query = query.split('who')[1]
            

            result = wikipedia.summary(query,sentences = 2)
            print(result)

            speak(result)
        elif 'news' in query:
            news_headlines = get_news_headlines()
            
            speak("Here are the top news headlines:")
            print(news_headlines)
            for headline in news_headlines:
                speak(headline)
       
        elif 'ipl score' in query:
            webbrowser.open('https://m.cricbuzz.com/')
        elif 'quote' in query:
            quote = get_random_quote()
            print(quote)
            speak(quote)

        elif 'open' in query:
            website = query.split(' ')[-1]
            url = f"https://www.{website}.com"
            webbrowser.open(url)
        elif 'search' in query:
            search_query = query.split(' ')[-1]
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
        elif 'weather' in query:
            location = query.split(' ')[-1]
            url = f"https://wttr.in/{location}?format=%C\n%t"
            response = requests.get(url)
            if response.status_code == 200:
                weather = response.text.strip()
                print(weather)
                speak(f"The current weather in {location} is {weather}")
            else:
                speak("Error fetching weather information")
            
        elif 'joke' in query:
            response = requests.get("https://official-joke-api.appspot.com/random_joke")
            if response.status_code == 200:
                data = response.json()
                joke = f"{data['setup']} {data['punchline']}"
                speak(joke)
            else:
                speak("Error fetching joke")
        elif 'notepad' in query:
            c1 = r'C:\\Windows\\System32\\notepad.exe'
            os.startfile(c1)
        
        elif "definition" in query:

            words = query.split()
            if "of" in query or 'what is' in query or 'meaning' in query:
                words = query.split()
                word_index = words.index("of") + 1
                word = words[word_index]
                definition = get_definition(word)
                print(definition)
                speak(f"The definition of {word} is: {definition}")
            else:
                speak("Please provide a word to define.")

        if "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif "send whatsapp message" in query:
            speak(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
        elif 'my ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')
            
        elif ('shutdown the system' in query) or ('down the system' in query):
             speak("Boss shutting down the system in 10 seconds")
             time.sleep(10)
             os.system("shutdown /s /t 5")
        elif 'tell me something' in query:
            speak(' I don\'t have much to say, you tell me someting i will give you the company')
        #elif 'thank you' in query:
            #speak('I am here to help you..., your welcome')
        elif 'hear me' in query:
            speak('Yes , I can hear you')
        elif 'rvr' in query:
            speak("Opening RVR & JC college, Official website")
            webbrowser.open('http://www.rvrjc.ac.in/')
        elif ' fees' in query:
            speak("OK sir , Opening portal for paying your college fees")
            webbrowser.open('https://rvrjcce.ac.in/tuitionfee/tuitionfee.php')
       
            
        if 'thank you' in query:
            speak("Your welcome, ")
       
        elif ('command prompt'in query) :
            speak('Opening command prompt')
            os.system('start cmd')
        elif 'your friend' in query:
            speak('My friends are Google alexa and siri')

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = command()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()
        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())
        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            translate(command())
        elif 'how are you' in query:
            speak("i am good,what about you?")
            listen = command()
            if 'good' in listen or 'fine' in listen:
                speak("Yup !!, Thats so great")
            if 'sad' in listen:
                speak("Its ok, dont worry, everything will be alright ")
        elif 'good job'in query:
            speak("Thank you, That's so sweet of you")
        elif 'schedule' in query or 'timetable' in query or 'todays classes' in query or 'periods' in query:
            shedule()
        elif 'social media' in query:
            social()
        elif 'translate' in query:
            translate()
            """
        
            """
        elif 'bf' in query:
            speak("Yes sure, here is my boy friend , he can `answer many questions and his name is Bard......hey bard, Here's someone for you")
            run_bradd()
        
        else:
            print("Chatting")
            #This is Chatgpt speaking with you , to awake Bard AI please say "BF" in Query 
            chat(query)