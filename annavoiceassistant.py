import pyttsx3 #convert text to speech
import speech_recognition as sr #speechRecognition
import datetime
import wikipedia 
import webbrowser#use for searching
import os
import subprocess 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!!")   

    else:
        speak("Good Evening!!")

    print('I am Anna.Mam,please tell me how may i help you')
    speak("I am Anna. Mam! Please tell me how may I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        speak("Say that again please...")      
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif'open calculator'in query:
            subprocess.call('calc.exe')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif'open notepad'in query:
            subprocess.call('notepad.exe')

        elif 'open overflow' in query:
            webbrowser.open("stackoverflow.com")
             
        elif'open spotify'in query:
            webbrowser.open('spotify.com') 

        elif'play music'in query:
            music_dir = 'c:\\Users\\LENOVO\\Music\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif'open github'in query:
            webbrowser.open("github.com")

        elif'open gpt' in query:
            webbrowser.open("chatgpt.com")

        elif'open paint' in query:
            subprocess.call('mspaint.exe')
        
        elif'open microsoft edge' in query:
            subprocess.call("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

         
            
    
        elif'stop'in query:
            speak('Thank you')
            break
    
        
