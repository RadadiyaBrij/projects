import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os 


def open_link(link_path):
 os.startfile(link_path)
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour==0 and hour<12:
        speak("Good morning!")
    elif hour == 12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")

def takecommand():
    #microphone input from user
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language ='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    speak("I am jarvis.How can i help you?")
    while True:
        query= takecommand().lower()  

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            if not query:
               speak("What should I search on Wikipedia?")
               query = takecommand().lower()
            try:
              results = wikipedia.summary(query, sentences=5)
              print(results)
              speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
             speak("There are multiple results for that topic. Please be more specific.")
             print("Options:", e.options)

            except wikipedia.exceptions.PageError:
             speak("Sorry, I couldn’t find any page about that. Please try another topic.")
             print("Page not found. Listening again...")

            except Exception as e:
             speak("An error occurred while searching. Please try again.")
             print(f"Error: {e}")
        
        elif 'open youtube' in query:
            # webbrowser.open("youtube.com") 
            open_link(r"https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open chrome' in query:    
            open_link(r"C:\Users\BAPS\OneDrive\Desktop\Brij - Chrome.lnk")

        elif 'open jioSaavn' in query:    
            open_link(r" C:\\Users\\BAPS\\OneDrive\\Desktop\\JioSaavn.lnk ")

        elif 'open whatsapp' in query:    
            open_link(r"C:\Users\BAPS\OneDrive\Desktop\WhatsApp.lnk")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            vscodepath ="C:\\Users\\BAPS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodepath) 
