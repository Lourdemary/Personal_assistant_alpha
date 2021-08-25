import operator
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import requests
import pyautogui
import instaloader
import os.path
import PyPDF2
from bs4 import  BeautifulSoup
from pywikihow import search_wikihow
import psutil
import speedtest
from twilio.rest import  Client
import datetime
import winsound





#text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[ len(voices) - 1].id)
engine.setProperty('rate',200)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=8, phrase_time_limit=8)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    query = query.lower()
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    tt = time.strftime("%m-%d-%Y %H:%M%p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am alpha. please tell me how may i help you")

# for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=a1b6bc610a13416c94d3ea706258c67c'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

def pdf_reader():
    book = open("",'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total numbers of pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number :"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

    # main program

def Whatsapp():
    speak("tell me the name of the person")
    name = takecommand()

    if 'Amrutha' in name:
        speak("tell me the message")
        msg = takecommand()
        speak("tell me the time sir")
        speak("tell me in hour")
        hour = int(takecommand())
        speak("time in minutes")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+917204453064", msg, hour, min, 20)
        speak("okay sir, sending whatsapp message")

    elif 'Dharani' in name:
        speak("tell me the message")
        msg = takecommand()
        speak("tell me the time sir")
        speak("tell me in hour")
        hour = int(takecommand())
        speak("time in minutes")
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+917204453064", msg, hour, min, 20)
        speak("okay sir, sending whatsapp message")

    else:
        speak("tell me the phone number")
        phone = int(takecommand())
        ph = '+91' + phone
        speak("tell me the message")
        msg = takecommand()
        speak("tell me the time sir")
        speak("tell me in hour")
        hour = int(takecommand())
        speak("time in minutes")
        min = int(takecommand())
        pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
        speak("okay sir, sending whatsapp message")

def OpenApps():
    speak("okay sir, wait a second")

    if "notepad" in query:
        os.startfile("c:\\windows\\system32\\notepad.exe")

    elif "open command prompt" in query:
        os.system("start cmd")

    elif "facebook" in query:
        webbrowser.open('https://www.facebook.com/')

    elif "open youtube" in query:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")

    elif "open stack overflow" in query:
        speak("opening facebook")
        webbrowser.open("https://www.stackoverflow.com")

    speak("your command has been successfully completed")

def CloseApps():
    speak("okay sir , wait a second")

    if "youtube" in self.query:
        os.system("TASKKILL /f /im chrome.exe")

def YoutubeAuto():
    speak("whats your command")
    comm = takecommand()

    if "pause" in comm:
        keyboard.press('space bar')

    elif "restart" in comm:
        keyboard.press('0')

    elif "mute" in comm:
        keyboard.press('m')

    elif "skip" in comm:
        keyboard.press('1')

    elif "back" in comm:
        keyboard.press('j')

    elif "full screen" in comm:
        keyboard.press('f')

    elif "film mode" in comm:
        keyboard.press('t')

    speak("done sir")

def ChromeAuto():
    speak("Chrome automation started")

    command = takecommand()

    if "close this tab" in command:
        keyboard.press_and_release('ctrl+w')

    # add others also

def Dict():
    speak("Activated Dictionary")
    speak("tell me the problem")
    prob1 = takecommand()

    if "meaning" in prob1:
        prob1 = prob1.replace("what is the", "")
        prob1 = prob1.replace("Alpha", "")
        prob1 = prob1.replace("of")
        prob1 = prob1.replace("meaning of", "")
        result = Diction.meaning(prob1)
        speak(f"the meaning of {prob1} is {result}")

    elif "antonym" in prob1:
        prob1 = prob1.replace("what is the", "")
        prob1 = prob1.replace("Alpha", "")
        prob1 = prob1.replace("of")
        prob1 = prob1.replace("antonym of", "")
        result = Diction.antonym(prob1)
        speak(f"the antonym of {prob1} is {result}")

    elif "synonym" in prob1:
        prob1 = prob1.replace("what is the", "")
        prob1 = prob1.replace("Alpha", "")
        prob1 = prob1.replace("of"."")
        prob1 = prob1.replace("synonym of", "")
        result = Diction.synonym(prob1)
        speak(f"the synonym of {prob1} is {result}")

    speak("Exited Dictionary")

def Task_Gui():
    wish()
    while True:
        # if 1:

        query = takecommand()

        #general questions
        if "hi" in query or "hello " in query:
            speak('hello sir, how may i help you?')

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        elif "who are you " in query:
            speak("i am alpha, i am your personal assistant")

        elif "who made you" in query or "who created you" in query:
            speak("i was created by mary ")

        elif "what can you do" in query:
            speak("i can do lots of things, for example you can ask me time, date, "
                  "weather in your city,i can open websites for you, launch application and more.")



        # logic building for tasks

        elif "open notepad" in query:
            speak("opening notepad")
            npath ="c:\\windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(20)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir="c:\\users\\91759\\pycharmprojects\\music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            speak("opening facebook")
            webbrowser.open("www.facebook.com")

        elif "open stack overflow" in query:
            speak("opening facebook")
            webbrowser.open("www.stackoverflow.com")

        elif "play song on youtube" in query:
            kit.playonyt("see you again")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+918105046232", "this is testing protocol", 16, 20)
            time.sleep(30)
            speak("message has been sent")

        # to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'timer' in query or 'stopwatch' in query:
            speak("for how many minutes?")
            timing = takecommand()
            timing = timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'i will remind you in {timing} seconds')
            time.sleep(timing)
            speak('your time has been finished sir')

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,setsuspendstate 0,1,0")

        elif "where am i " in query or "where are we" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                url = "https://get.geojs.io/v1/ip/geo/" +ipAdd+".json"
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print (geo_data)
                city = geo_data["city"]
                #state = geo_data["state"]
                country = geo_data["country"]
                speak(f"sir i am not sure, but i think we are in {city} city of  {country} country ")
            except Exception as e:
                speak("sorry sir due to network issue i am not able to find where we are")
                pass

        elif "instagram profile " in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly")
            name = input("enter username here :")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir , profile picture is saved in our main folder, now i am ready for next command")
            else:
                pass

        #to take screenshot
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir , the screenshot is saved in our main folder, now i am ready for the next command")

        elif "read pdf " in query:
            pdf_reader()

        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide" in condition :
                os.system("attrib +h /s /d")
                speak("sir all the files in the folder are now hidden")
            elif "visible " in condition:
                os.system("attrib -h /s /d")
                speak("sir all the files in the folder are now visible to everyone. I wish you are taking the risk on your own")

            elif "leave it" in condition or "leave for now" in condition:
                speak("okay sir")

        elif "do some calculations" in query or "can you calculate " in query:
            r = sr.Recognizer()
            with sr.Microphone() as source :
                speak(" Say what you want to calculate , example 3 plus 3 ")
                print("Listening")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string= r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                }[op]
            def eval_binary_expr(op1,oper,op2):
                op1,op2= int(op1), int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))

        elif " how are you " in query:
            speak("i am fine sir, what about you")

        elif " also good" in query:
            speak(" thats good to hear from you")

        elif "thank you" in query or " thanks" in query:
            speak("Its my pleasure sir")

        elif " you can sleep" in query or "sleep now" in query :
            speak("okay sir , i am going to sleep ,you can call me anytime")
            break

        elif "temperature" in query:
            search = "Temperature in Bangalore"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "activate how to do mode" in query:
            speak("How to do mode is activated please tell me what you want to know")
            how = takecommand()
            max_results = 1
            how_to = search_wikihow(how,max_results)
            assert len(how_to) ==1
            how_to[0].print()
            speak(how_to[0].summary)

        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system has{percentage} percent battery")
            if percentage>=75:
                speak("we have enough power  to continue our work")
            elif percentage>=40 and percentage <= 75:
                speak("We should connect our system to charging point to charge our battery")
            elif percentage>=15 and percentage<=40:
                speak("We dont have enough power to work, please connect to charging")
            elif percentage<=15:
                speak("we have very low power, please connect to charging else the system will shutdown very soon")


        elif "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
            #try :
             #   os.system('cmd /k "speedtest" ' )
            #except:
             #   speak(f"there is no internet connection")


        elif "send message" in query :
            speak("Sir what should I say ")
            msz = takecommand()

            account_sid = 'AC9756cb0d54621164a277e2456e984ed5'
            auth_token = '3c9ea1d22e0ad717858d50225e309d1a'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body='This is the ship that made the Kessel Run in fourteen parsecs?',
                from_='+18507798742', #both number should be verified by twilio(to number also should be verified)
                to='+1918105046232'
            )

            print(message.sid)


        elif "make a call" in query :

            account_sid = 'AC9756cb0d54621164a277e2456e984ed5'
            auth_token = '3c9ea1d22e0ad717858d50225e309d1a'
            client = Client(account_sid, auth_token)

            message = client.calls \
                .create(
                    twiml='<Response><Say> this is a testing call from Alpha ....</Say></Response>',
                    from_='+18507798742', #both number should be verified by twilio(to number also should be verified)
                    to='+918105046232'
                )
            print(message.sid)

        elif " volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")

        elif "open mobile camera" in query :
            import urllib.request
            import cv2
            import numpy as np
            import time
            URL = "http://192.168.225.115:8080/video" #mary
            #URL = "http://56.183.113.24:8080/video" #Bubesh
            cap=cv2.VideoCapture(URL)
            while True:
                ret, frame=cap.read()
                if frame is not None:
                    cv2.imshow('frame',frame)
                q=cv2.waitKey(1)

                #img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                #img = cv2.imencode(img_arr, -1)
                #cv2.imshow('IPWebcam',img)
                #q = cv2.waitKey(1)
                if q == ord("q"):
                    break;

            cv2.destroyAllWindows()


        elif "youtube search" in query:
            speak("okay sir this is what i found for your search")
            query = query.replace("alpha", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("done sir")

        elif "website" in query:
            speak("okay sir , launching.....")
            query = query.replace("Alpha", "")
            query = query.replace("website")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("launched")

        elif "open youtube" in query:
            OpenApps()

        elif "open facebook" in query:
            OpenApps()

        elif "open stack overflow" in query:
            OpenApps()

        elif "whatsapp message" in query:
            Whatsapp()

        elif "pause" in query:
            keyboard.press('space bar')

        elif "restart" in query:
            keyboard.press('0')

        elif "mute" in query:
            keyboard.press('m')

        elif "skip" in query:
            keyboard.press('1')

        elif "back" in query:
            keyboard.press('j')

        elif "full screen" in query:
            keyboard.press('f')

        elif "film mode" in query:
            keyboard.press('t')

        elif "pause" in query:
            keyboard.press('k')

        elif "youtube tool" in query:
            YoutubeAuto()

        elif "Chrome tool" in query:
            ChromeAuto()

        elif "dictionary" in query:
            Dict()



# speak("sir, do you have any other work")
