import pyttsx3 #text-to-speech
import datetime
import speech_recognition as sr 
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyjokes
import pyautogui
import psutil

engine = pyttsx3.init(driverName='sapi5')
engine.setProperty('rate',180)

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# Use female voice 
engine.setProperty('voice', voice_id)


def speak(phrase):
    #audio output for the command using pyttsx3
    engine.say(phrase)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is ")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = datetime.datetime.now().strftime("%d :%B")
    speak("Today is ")
    speak(month)
    speak(year)

def greet():
    speak("Welcome back sir!")
    time()
    date()
    speak("How can I help you?")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('cylopsai@gmail.com','cylopsai1234')
    server.sendmail('cylopsai@gmail.com',to,content)
    server.close()

def jokes():
    speak("Here is one for you ")
    speak(pyjokes.get_joke())

def screenshot():
    screen_img = pyautogui.screenshot()
    screen_img.save(r'C:\Users\dhira\OneDrive\Desktop\Cradle\Images\ss.png')
    speak("Ok! I took a screenshot")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("Current CPU usage at ; " +usage + " percent.")
    battery = psutil.sensors_battery()
    speak("Battery level at " + str(battery.percent) + " percent.")


def get_command():
    speech = sr.Recognizer()
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source,duration=1)
        print("Listening.... ")
        audio = speech.listen(source)

    try:
        print("Recognizing...")
        query = speech.recognize_google(audio)
        print(query)

    except Exception as E:
        print(E)
        speak("I couldn't get it!")
        get_command()

    return query

if __name__ == "__main__":
    greet()
    while True:
        query = get_command().lower()

        if 'time' in query or 'what' in query:
            time()

        elif 'date' in query or 'day' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching on wikipedia ...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'mail'in query or 'email' in query:
            try:
                speak("What should the message be?")
                content = get_command()
                speak("Whom to send to?")
                to = input("Enter email -id of the reciever")
                sendEmail(to,content)
                speak("Ok! The message is sent")
            
            except Exception as E:
                print(E)
                speak("Unable to send email. Please check logs for more info.")

        elif 'search' in query or 'chrome' in query:
            speak("What should I search for?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            content = get_command().lower()
            wb.get(chromepath).open_new_tab(content)

        elif 'logout' in query:
            prompt = input("Enter 'y' to logout of system or 'n' to abort \n")
            if prompt.lower() == 'y':
                os.system("shutdown -l")
            else:
                continue
        
        elif 'shutdown' in query:
            prompt = input("Enter 'y' to shutdown system or 'n' to abort \n")
            if prompt.lower() == 'y':
                os.system("shutdown /s /t 1")
            else:
                continue

        elif 'restart' in query:
            prompt = input("Enter 'y' to restart system or 'n' to abort \n")
            if prompt.lower() == 'y':
                os.system("shutdown /r /t 1")
            else:
                continue

        elif 'song' in query and 'play' in query:
            music_dir = r"C:\Users\dhira\OneDrive\Documents\Rockstar Games\GTA V\User Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'joke' in query or 'jokes' in query:
            jokes()

        elif 'screenshot' in query:
            screenshot()

        elif 'cpu' in query or 'battery' in query:
            cpu()

        elif 'offline' in query:
            speak("Okay! Have a good day!")
            quit()