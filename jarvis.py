import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[1].id)

engine.setProperty('voice', voice[1].id)


def speak(audio):
     engine.say(audio)
     engine.runAndWait()


def wish():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("good morning sir")
        elif hour >= 12 and hour < 18:
            speak("good after noon sir")
        elif hour > 18:
            speak("good after noon sir")

        speak("i am jarvis how can i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        audio = r.listen(source)

    try:
        print("Recognizeing...")
        query = r.recognize_google(audio, language='en-us')
        print("You said  :-", query)

    except Exception as e:
        print(e)
        print("say that again please..")
        return"None"
    return query


if __name__ == "__main__":
    wish()
    
    while True:
        
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching for wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("accoding to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new_tab("www.youtube.com")

        elif 'play music' in query:
            music_die = 'D:\\Music'
            song = os.listdir(music_die)
            os.startfile(os.path.join(music_die, song[0]))

        elif 'open my computer' in query:

             os.startfile(
                 'C:\\Users\\KHUNT JAY\\Desktop\\This PC - Shortcut.lnk')

        elif 'open google' in query:
            os.startfile(
                'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

        elif 'open new tab' in query:
            webbrowser.open_new_tab('www.google.com')

        elif 'open browser' in query:
            webbrowser.Chrome('chrome')

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"sir the time is {time}")

        elif 'shutdown pc' in query:
            os.system('shutdown /s /t 5')

        elif 'restart pc' in query:
            os.system('shutdown  /r  /t  3')
       
        
        elif 'exit'in query:
            speak('thanks to use jarvis ')
            exit()
         
 



        
            
    
       
   
