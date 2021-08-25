from alphaGUI import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
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
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import speedtest
from twilio.rest import Client
import datetime
import winsound
import keyboard
from playsound import playsound
from PyDictionary import PyDictionary as Diction
import PyPDF2
from googletrans import Translator





# text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[len(voices) - 1].id)
engine.setProperty('rate', 200)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Task_Gui()

    def takecommand(self):
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

    def Task_Gui(self):



        speak("i am alpha. please tell me how may i help you")

        while True:
            # if 1:

            self.query = self.takecommand()

            # general questions
            if "hi" in self.query or "hello " in self.query:
                speak('hello sir, how may i help you?')

            elif "no thanks" in self.query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()

            elif "who are you " in self.query:
                speak("i am alpha, i am your personal assistant")

            elif "who made you" in self.query or "who created you" in self.query:
                speak("i was created by mary ")

            elif "what can you do" in self.query:
                speak("i can do lots of things, for example you can ask me time, date, "
                      "weather in your city,i can open websites for you, launch application and more.")

            # logic building for task
            elif "open notepad" in self.query:
                speak("opening notepad")
                npath = "c:\\windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")


            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "close command prompt" in self.query:
                os.system("taskkill /f /im cmd.exe")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(20)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:
                music_dir = "C:\\Users\\91759\\PycharmProjects\\Alpha\\Music"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)

            elif "open youtube" in self.query:
                speak("opening youtube")
                webbrowser.open("www.youtube.com")

            elif "open geeks for geeks" in self.query:
                speak("opening geeks for geeks")
                webbrowser.open("https://www.geeksforgeeks.org")

            elif "open tutorials point" in self.query:
                speak(" tutorials point")
                webbrowser.open("www.tutorialspoint.com")

            elif "open twitter" in self.query:
                speak("opening twitter")
                webbrowser.open("www.twitter.com")

            elif "open facebook" in self.query:
                speak("opening facebook")
                webbrowser.open("www.facebook.com")

            elif "open stack overflow" in self.query:
                speak("opening stack over flow")
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "send whatsapp message" in self.query:
                kit.sendwhatmsg("+918105046232", "this is testing protocol", 16, 20)
                time.sleep(30)
                speak("message has been sent")

            # to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'timer' in self.query or 'stopwatch' in self.query:
                speak("for how many minutes?")
                timing = self.takecommand()
                #timing = timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'i will remind you in {timing} seconds')
                time.sleep(timing)
                speak('your time has been finished sir')

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait sir, fetching the latest news")
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

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,setsuspendstate 0,1,0")

            elif "where am i " in self.query or "where are we" in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get("https://api.ipify.org").text
                    print(ipAdd)
                    url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + ".json"
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print (geo_data)
                    city = geo_data["city"]
                    # state = geo_data["state"]
                    country = geo_data["country"]
                    speak(f"sir i am not sure, but i think we are in {city} city of  {country} country ")
                except Exception as e:
                    speak("sorry sir due to network issue i am not able to find where we are")
                    pass

            elif "instagram profile " in self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly")
                name = input("enter username here :")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak(
                        "i am done sir , profile picture is saved in our main folder, now i am ready for next command")
                else:
                    pass

            # to take screenshot
            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("sir please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("please sir hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir , the screenshot is saved in our main folder, now i am ready for the next command")

            elif "read pdf " in self.query or "read notes" in self.query or "audiobook" in query:
                book = open("C:\\Users\\91759\\PycharmProjects\\Alpha\\Tutorial_EDIT.pdf", 'rb')
                pdfReader = PyPDF2.PdfFileReader(book)
                pages = pdfReader.numPages
                speak(f"total numbers of pages in this book {pages}")
                speak("sir please enter the page number i have to read")
                pg = int(input("please enter the page number :"))
                page = pdfReader.getPage()
                text = page.extractText()
                speak(text)


            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("sir all the files in the folder are now hidden")
                elif "visible " in condition:
                    os.system("attrib -h /s /d")
                    speak(
                        "sir all the files in the folder are now visible to everyone. I wish you are taking the risk on your own")

                elif "leave it" in condition or "leave for now" in condition:
                    speak("okay sir")

            elif "do some calculations" in self.query or "can you calculate " in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak(" Say what you want to calculate , example 3 plus 3 ")
                    print("Listening")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided': operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))

            elif " how are you " in self.query:
                speak("i am fine sir, what about you")

            elif " also good" in self.query:
                speak(" thats good to hear from you")

            elif "thank you" in self.query or " thanks" in self.query:
                speak("Its my pleasure sir")

            elif " you can sleep" in self.query or "sleep now" in self.query:
                speak("okay sir , i am going to sleep ,you can call me anytime")
                break

            elif "temperature" in self.query:
                search = "Temperature in Bangalore"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")

            elif "activate how to do mode" in self.query:
                speak("How to do mode is activated please tell me what you want to know")
                how = self.takecommand()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)

            elif "how much power left" in self.query or "how much power we have" in self.query or "battery" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system has{percentage} percent battery")
                if percentage >= 75:
                    speak("we have enough power  to continue our work")
                elif percentage >= 40 and percentage <= 75:
                    speak("We should connect our system to charging point to charge our battery")
                elif percentage >= 15 and percentage <= 40:
                    speak("We dont have enough power to work, please connect to charging")
                elif percentage <= 15:
                    speak("we have very low power, please connect to charging else the system will shutdown very soon")


            elif "internet speed" in self.query:
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
                # try :
                #   os.system('cmd /k "speedtest" ' )
                # except:
                #   speak(f"there is no internet connection")


            elif "send message" in self.query:
                speak("Sir what should I say ")
                msz = self.takecommand()

                account_sid = 'AC9756cb0d54621164a277e2456e984ed5'
                auth_token = '3c9ea1d22e0ad717858d50225e309d1a'
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body='This is the ship that made the Kessel Run in fourteen parsecs?',
                    from_='+18507798742',  # both number should be verified by twilio(to number also should be verified)
                    to='+1918105046232'
                )

                print(message.sid)


            elif "make a call" in self.query:

                account_sid = 'AC9756cb0d54621164a277e2456e984ed5'
                auth_token = '3c9ea1d22e0ad717858d50225e309d1a'
                client = Client(account_sid, auth_token)

                message = client.calls \
                    .create(
                    twiml='<Response><Say> this is a testing call from Alpha ....</Say></Response>',
                    from_='+18507798742',  # both number should be verified by twilio(to number also should be verified)
                    to='+918105046232'
                )
                print(message.sid)

            elif " volume up" in self.query:
                pyautogui.press("volumeup")

            elif "volume down" in self.query:
                pyautogui.press("volumedown")

            elif "volume mute" in self.query or "mute" in self.query:
                pyautogui.press("volumemute")

            elif "open mobile camera" in self.query:
                import urllib.request
                import cv2
                import numpy as np
                import time
                URL = "http://192.168.225.115:8080/video"  # mary
                # URL = "http://56.183.113.24:8080/video" #Bubesh
                cap = cv2.VideoCapture(URL)
                while True:
                    ret, frame = cap.read()
                    if frame is not None:
                        cv2.imshow('frame', frame)
                    q = cv2.waitKey(1)

                    # img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                    # img = cv2.imencode(img_arr, -1)
                    # cv2.imshow('IPWebcam',img)
                    # q = cv2.waitKey(1)
                    if q == ord("q"):
                        break;

                cv2.destroyAllWindows()


            elif "youtube search" in self.query:
                speak("okay sir this is what i found for your search")
                self.query = self.query.replace("alpha", "")
                self.query = self.query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + self.query
                webbrowser.open(web)
                speak("done sir")

            elif "website" in self.query:
                speak("okay sir , launching.....")
                self.query = self.query.replace("Alpha", "")
                self.query = self.query.replace("website")
                web1 = self.query.replace("open", "")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                speak("launched")

            elif "open youtube" in self.query:
                speak("okay sir, wait a second")
                webbrowser.open('https://www.youtube.com/')

            elif "open facebook" in self.query:
                speak("okay sir, wait a second")
                webbrowser.open('https://www.facebook.com/')

            elif "open stack overflow" in self.query:
                speak("okay sir, wait a second")
                webbrowser.open('https://www.stackoverflow.com/')

            elif "whatsapp message" in self.query:
                Whatsapp()

            elif "alarm " in self.query or "set alarm" in self.query:
                speak("enter the time")
                time = input(": enter the time:")
                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")
                    if now == time:
                        speak("time to wake up maam")
                        playsound("C:\\Users\\91759\\PycharmProjects\\Alpha\\alarm\\siri_morning_wake_up.mp3")
                        speak("Alarm closed")
                    elif now>time:
                        break


            elif "Chrome tool" in self.query or "open chrome" in self.query:
                speak("opening , please wait")
                webbrowser.open("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                speak("Chrome launched")


            elif "dictionary" in self.query or "search in dictionary" in self.query:
                speak("Activated Dictionary")
                speak("tell me the problem")
                prob1 = self.takecommand()

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
                    prob1 = prob1.replace("of", "")
                    prob1 = prob1.replace("synonym of", "")
                    result = Diction.synonym(prob1)
                    speak(f"the synonym of {prob1} is {result}")

                speak("Exited Dictionary")

            #elif "translate" in self.query:
             #   translator = Translator()
              #  line = "Bengaluru (also called Bangalore) is the capital of India's southern Karnataka state. The center of India's high-tech industry, the city is also known for its parks and nightlife. By Cubbon Park, Vidhana Soudha is a Neo-Dravidian legislative building. Former royal residences include 19th-century Bangalore Palace, modeled after England’s Windsor Castle, and Tipu Sultan’s Summer Palace, an 18th-century teak structure. "
               # out = translator.translate(line, dest='kn')
                #print(out.text)
                #speak(out.text)



startFunctions = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):
        super(Gui_Start, self).__init__()
        self.alpha_ui = Ui_MainWindow()
        self.alpha_ui.setupUi(self)

        self.alpha_ui.pushButton.clicked.connect(self.startFunc)
        self.alpha_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        self.alpha_ui.movies_label_2 = QtGui.QMovie("Images/initiating.gif")
        self.alpha_ui.label_2.setMovie(self.alpha_ui.movies_label_2)
        self.alpha_ui.movies_label_2.start()

        self.alpha_ui.movies_label_3 = QtGui.QMovie("Images/OccasionalBonyDugong-max-1mb.gif")
        self.alpha_ui.label_3.setMovie(self.alpha_ui.movies_label_3)
        self.alpha_ui.movies_label_3.start()

        self.alpha_ui.movies_label_4 = QtGui.QMovie("../../Downloads/GIF-210730_235808.gif")
        self.alpha_ui.label_4.setMovie(self.alpha_ui.movies_label_4)
        self.alpha_ui.movies_label_4.start()

        self.alpha_ui.movies_label_6 = QtGui.QMovie("Images/gif.gif")
        self.alpha_ui.label_6.setMovie(self.alpha_ui.movies_label_6)
        self.alpha_ui.movies_label_6.start()

        startFunctions.start()


Gui_App = QApplication(sys.argv)
Gui_alpha = Gui_Start()
Gui_alpha.show()
exit(Gui_App.exec_())
