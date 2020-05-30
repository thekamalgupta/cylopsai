import pyttsx3 #text-to-speech
import datetime
import speech_recognition as sr #speech recognition
import wikipedia #python wikipedia module for wikipedia api
import smtplib #mail server
import webbrowser as wb #open in chrome
import os #logout,shutdown and restart
import pyjokes #jokes module
import pyautogui #screenshot function
import psutil #cpu and battery stats

#pyttsx3 setup
engine = pyttsx3.init(driverName='sapi5')
engine.setProperty('rate',180)

#female voice id
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# Use female voice 
engine.setProperty('voice', voice_id)


def speak(phrase):
    #audio output for the command using pyttsx3
    engine.say(phrase)
    engine.runAndWait()

#current time in AM/PM format
def time():
    
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is ")
    speak(Time)

#current date in DD/Monthname/YY
def date():
    
    year = int(datetime.datetime.now().year)
    month = datetime.datetime.now().strftime("%d :%B")
    speak("Today is ")
    speak(month)
    speak(year)

#greetings function
def greet():
    #executes every time the program is loaded
    speak("Welcome back sir!")
    time()
    date()
    speak("How can I help you?")

#email functionality
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('cylopsai@gmail.com','cylopsai1234')
    server.sendmail('cylopsai@gmail.com',to,content)
    server.close()

#jokes using the pyjokes module
def jokes():
    speak("Here is one for you ")
    speak(pyjokes.get_joke())

#screenshot function through pyautogui
def screenshot():
    screen_img = pyautogui.screenshot()
    screen_img.save(r'C:\Users\dhira\OneDrive\Desktop\Cradle\Images\ss.png')
    speak("Ok! I took a screenshot")

#cpu and battery stats using psutil module
def cpu():
    usage = str(psutil.cpu_percent())
    speak("Current CPU usage at ; " +usage + " percent.")
    battery = psutil.sensors_battery()
    speak("Battery level at " + str(battery.percent) + " percent.")

#function to take speech input from user and convert to text using SpeechRecognizer
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

#main
if __name__ == "__main__":
    greet()
    while True:
        query = get_command().lower()

        if 'time' in query or 'what' in query:
            #give current time
            time()

        elif 'date' in query or 'day' in query:
            #give current date
            date()

        elif 'wikipedia' in query:
            #give wikipedia summary of query
            speak("Searching on wikipedia ...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'mail'in query or 'email' in query:
            #send mail by asking for content and reciepent from user
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
            #open in web browser
            speak("What should I search for?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            content = get_command().lower()
            wb.get(chromepath).open_new_tab(content)

        elif 'logout' in query:
            #logout from the system
            prompt = input("Enter 'y' to logout of system or 'n' to abort \n")
            if prompt.lower() == 'y':
                os.system("shutdown -l")
            else:
                continue
        
        elif 'shutdown' in query:
            #shutdown the system(!!It will shutdown the computer!!)
            prompt = input("Enter 'y' to shutdown system or 'n' to abort \n")
            if prompt.lower() == 'y':
                os.system("shutdown /s /t 1")
            else:
                continue

        elif 'restart' in query:
            #restart the computer
            prompt = input("Enter 'y' to restart system or 'n' to abort \n")
            if prompt.lower() == 'y':
                os.system("shutdown /r /t 1")
            else:
                continue

        elif 'song' in query and 'play' in query:
            #play song
            music_dir = r"C:\Users\dhira\OneDrive\Documents\Rockstar Games\GTA V\User Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'joke' in query or 'jokes' in query:
            #tell a joke
            jokes()

        elif 'screenshot' in query:
            #take a screenshot
            screenshot()

        elif 'cpu' in query or 'battery' in query:
            #give battery and cpu stats
            cpu()

        elif 'offline' in query:
            #exit the program :)
            speak("Okay! Have a good day!")
            quit()