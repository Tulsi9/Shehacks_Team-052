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
            speak("Opening Google.")
            webbrowser.open("google.com")

        
        elif 'play music' in query:
            music_dir = 'D:\\xyz\\songs\\abc'#path of your music directory
            songs = os.listdir(music_dir)
            print(songs) 
            os.startfile(os.path.join(music_dir, songs[0]))
            
            
        elif 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("youtube.com")
    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Ma'am , the time is ")
            speak(strTime)
            
            
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    
            

        elif 'open code' in query:
            speak("Opening Editor.")
            codePath = "C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #target of the application
            os.startfile(codePath)
            
            
        elif 'open stack overflow' in query:
            speak("Opening Stack overflow.")
            webbrowser.open("stackoverflow.com")   

            
        elif 'open amazon' in query :
            speak("Opening Amazon.")
            webbrowser.open("amazon.in")
            
          
        elif 'open hotstar' in query:
            speak("Opening Hotstar.")
            webbrowser.open("hotstar.com/in")
            

        elif 'send email to <someone> ' in query:
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
            speak("Thank you. Have a nice day!")
            break  
        
