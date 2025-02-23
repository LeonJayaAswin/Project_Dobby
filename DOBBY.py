import pyttsx3
import speech_recognition as SR
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r = SR.Recognizer()
    with SR.Microphone() as source:
        print("Dobby is Listening..")
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
        print("Dobby is Processing please wait for a moment..")
        query = r.recognize_google(audio,language='en-in')
        print(f"You just said: {query}\n")
    except Exception as e:
        print(e)
        print("Dobby Can't Catch Your Voice")
        speak("I can't catch you, can you please tell me again.")
        query="none"
    
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        print("Good Morning Boss.")
        speak("Good Morning Boss.")
    elif hour >=12 and hour<17:
        print("Good Afternoon Boss.")
        speak("Good Afternoon Boss.")
    elif hour >=17 and hour<21:
        print("Good Evening Boss.")
        speak("Good Evening Boss.")
    # else:
    #     print("Good Night Boss.")
    #     speak("Good Night Boss.")



if __name__== "__main__":
    wish()
    while True:
        query = commands().lower()
        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The Time is {strTime}")
            speak(f"The Time is {strTime} Sir..")
            
        elif "open Brave" in query:
            speak("Opening Brave Boss.")
            print("Opening Brave.")
            os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
             
        # elif "open spotify" in query:
        #     speak("Opening Spotify Boss.")
        #     print("Opening Spotify..")
        #     os.startfile()
        
        #greeting  dobby
        elif "good morning" in query or "good afternoon" in query or "good evening" in query:
             speak("How can I help You Boss?")
        elif "good night" in query:
             speak("Good Night Boss.")


        # Encourage dobby
        elif "Good" in query or "awesome" in query:
            speak("Thank You Boss, It's good to getting Good words from you.")





        elif "search" in query:
            try:
                speak("Searching in Wikipedia Boss.")
                query = query.replace("search", "").strip()
        
        # Find closest matching page title
                search_results = wikipedia.search(query)
                if search_results:
                    best_match = search_results[0]  # Take the first matching result
                    results = wikipedia.summary(best_match, sentences=1)
                    print(results)
                    speak(f"According to Wikipedia, {results}")
                    
                else:
                     speak("No relevant results found on Wikipedia, Boss.")
                     print("No relevant results found.")
            except wikipedia.exceptions.DisambiguationError as e:
                 speak("Multiple results found. Please be more specific.")
                 print(f"Disambiguation Error: {e.options}")
            except wikipedia.exceptions.PageError:
                 speak("No relevant page found for this search boss.")
                 print("No Wikipedia page found.")
            except Exception as e:
                 print(f"An error occurred: {e}")
                 speak("Sorry Boss, I encountered an error while searching.")

        elif "play" in query:
            query=query.replace("play",'')
            speak(f"Playing {query} Boss.")
            print(f"Playing {query}.")
            pywhatkit.playonyt(query)
        elif 'type' in query:
            print("Dobby Is Ready To Type")
            while True:
                typequery = commands()
                if typequery in 'exit typing':
                    speak("Typing Done Boss")
                    print("Typing Done")
                    break
                else:
                    pyautogui.write(typequery)
        # Dobby joking commands
        elif 'joke' in query:
            jokes=pyjokes.get_joke()
            print(jokes)
            speak(jokes)

            # to minimize the app using dobby
        elif 'minimize' in query or 'minimise' in query:
            pyautogui.moveTo(1748,27)
            pyautogui.leftClick()
            # to maximize the app using dobby
        elif 'maximize' in query or 'maximise' in query:
            pyautogui.moveTo(1816,16)
            pyautogui.leftClick()
            # to close the app using dobby
        elif 'close' in query:
            pyautogui.moveTo(1896,31)
            pyautogui.leftClick()

        # exit dobby
        elif 'exit program' in query or 'exit the program' in query or "shut up" in query:
            speak("Roger That Boss.")
            print("Dobby is went to sleep")
            quit()








