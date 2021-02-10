import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import subprocess
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):                                
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time) 

def date():
    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Day = datetime.datetime.now().day
    speak("The current date is")
    speak(Day)
    speak(Month)
    speak(Year)

def greet():
    speak("Welcome back sir")
    hour = datetime.datetime.now().hour
    if hour>6 and hour<12:
        speak("A Good morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    elif hour>18 and hour<24:
        speak("Good evening")
    else:
        speak("Its been late, you should probably sleep now but anyways")
    speak("Jarvis at your service, Please tell me how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('sidrock31@gmail.com','sidkareena')
        server.sendmail('sidrock31@gmail.com', to, content)
        server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\Win10\\Pictures\\Screenshots\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)    

def joke():
    speak(pyjokes.get_joke())

if __name__ == '__main__':
    greet()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
        
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        
        elif 'send a email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = 'siddharth.y110397@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")

        elif "log off" in query or "logoff" in query:
            speak("Ok , your pc is logging off")
            subprocess.call(["shutdown", "/l"])
        
        elif 'open youtube' in query:
            wb.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")     

        elif 'open google' in query:
            wb.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")        

        elif 'open gmail' in query:
            wb.open_new_tab("gmail.com")
            speak("Gmail is open now")

        elif 'play songs' in query:
            songs_dir = 'E:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you told me to remember that" + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'cpu' in query:
            cpu()
        
        elif 'joke' in query:
            joke()

        elif 'offline' in query:
            speak("Goodbye Sir")
            quit()
            


        
        


