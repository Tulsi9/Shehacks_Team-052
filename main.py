import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Processing")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)

    except Exception as e:
         
        print("Say that again please...")  
        return "None"
    return query

def Email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    
    speak("I am Friday. Please, tell me how may I help you today?")       
    

if __name__ == "__main__":
    Greetings()
    while True:
    
        query = takeCommand().lower()
        
        if 'open google' in query:
            webbrowser.open("google.com")

        
        elif 'play music' in query:
            music_dir = 'D:\\xyz\\songs\\abc'#path of your music directory
            songs = os.listdir(music_dir)
            print(songs) 
            speak('Which song number do you want me to play')
            num = takeCommand()
            os.startfile(os.path.join(music_dir, songs[num-1]))
            
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is ",strTime)
            
            
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    
            

        elif 'open code' in query:
            codePath = "C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #target of the application
            os.startfile(codePath)
            
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

            
        elif 'open amazon' in query :
            webbrowser.open("amazon.in")
            
          
        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com/in")
            

        elif 'email ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "YourEmail@gmail.com"    
                Email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Ma'am. I am not able to send this email.")   
                
                
        elif 'bye' in query or 'quit' in query :
            exit() 
        
