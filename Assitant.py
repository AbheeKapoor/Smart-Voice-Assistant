import datetime
import re
from time import time
from urllib import parse
import bs4
from h11 import Data
from playsound import playsound
from gtts import gTTS
import pyperclip
import pywhatkit
import requests
from PyQt5.QtCore import QThread
from bs4 import BeautifulSoup
import wikipedia
import os
import webbrowser as web
import random
import datetime
from VoiceEngine import VoiceCore
from automation import whatsappCall, whatsappChat
import pyjokes
import pyautogui
from time import sleep
import cv2
import psutil
import numpy as np
import time
import pyautogui
import urllib.request
import speedtest
from plyer import notification




def extract_title(url):
    p = parse.urlparse(url, 'http')
    netloc = p.netloc or p.path
    path = p.path if p.netloc else ''
    if not netloc.startswith('www.'):
        netloc = 'www.' + netloc
    p = parse.ParseResult('https', netloc, path, *p[3:])
    url = p.geturl()
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.title.string


class core(QThread):
    def __init__(self, main_window, voice, name):
        super().__init__()
        self.main_window = main_window
        self.name = name
        self.voice = voice
        self.input_string = ''

    def process(self, string):

        response = ''
        string = string.lower()

        # Checking Conditions
        if 'tell me about' in string or 'search about' in string or 'search' in string:
            string = string.replace('tell me about', '')
            string = string.replace('search about', '')
            string = string.replace('search', '')

            # response = 'Searching for {}'.format(string)

            string = '+'.join(string.split())
            url = 'http://www.google.com/search?q=' + string
            response = extract_title(url)

            self.respond(response)
            print(url)
            self.main_window.open_url(url)

        elif 'time' in string:
            response = 'The Time is {}'.format(datetime.datetime.now().strftime('%I %M %p'))  # %d %B, %Y'))
            self.respond(response)

        elif 'hello' in string:
            name=self.name
            
            hour=int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                self.respond(f"Good Morning {name} How Can I Help You")
            elif hour>=12 and hour<18:
                self.respond(f"Good Afternoon {name}  How Can I Help You")
            else:
                self.respond(f"Good Evening {name}  How Can I Help You")

        elif'how are you' in string:
            self.respond('I am Fine Sir and What About You')

        elif'what is your age'in string:
            self.respond('I am 6 Months Old')

        elif'battery'in string or 'how much power left'in string:
            
            battery=psutil.sensors_battery()
            percentage=battery.percent
            self.respond(f"Sir Our System Have {percentage} Percent Battery")
            if percentage>=75:
                self.respond("We have Enough Power to Continue with our Work")
            elif percentage>=40 and percentage<75:
                self.respond("We Should Charge The System")
            elif percentage>=15 and percentage<40:
                self.respond("We Dont Have Enough Battery To Continue With Work , Please Connect the Charger")
            elif percentage<15:
                self.respond("We Have Very Less Battery , Please Connect The Charger Otherwise The System Will Shut Down Very Soon")


        elif'internet speed' in string:
            st=speedtest.Speedtest()
            dl=st.download()*0.000000125
            up=st.upload()*0.000000125
            self.respond(f"Sir We Have {dl} MB Downloading Speed and {up}  MB Uploading Speed")

        elif'up' in string:  
            pyautogui.press("volumeup")
            self.respond('Done Sir')

        elif'down' in string:
            pyautogui.press("volumedown")
            self.respond('Done Sir')

        elif'mute' in string:
            pyautogui.press("volumemute")
            self.respond('Muted Sir')


        elif 'open' in string:
            reg_ex = re.search('open (.+)', string)
            self.main_window.open_url('www.' + reg_ex.group(1)+'.com')
            response = 'Opening ' + reg_ex.group(1)
            self.respond(response)

        elif'youtube' in string:
            self.respond('Opening Youtube')
            string=string.replace("youtube","")
            result="https://www.youtube.com//results?search_query="+string
            web.open(result)
            
        elif'cricket score' in string:
            url="https://www.cricbuzz.com/"
            page=requests.get(url)
            soup=BeautifulSoup(page.text,"html.parser")
            team1=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
            team2=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
            team1_score=soup.find_all(class_="cb-ovr-flo")[8].get_text()
            team2_score=soup.find_all(class_="cb-ovr-flo")[10].get_text()
            a=self.respond(f"{team1} : {team1_score}")
            b=self.respond(f"{team2} : {team2_score}")

            notification.notify(title ="ipl score :- ",message=f"{team1}:{team1_score} \n {team2} : {team2_score}",timeout=10)
        
        elif'news'in string:
            self.respond("Getting Today's News Sir , Wait For Few Seconds ")
            main_url='https://newsapi.org/v2/top-headlines?country=in&apiKey=a7fcfaef58374e108664c4992fb41e96'
            main_page=requests.get(main_url).json()
            
            articles=main_page["articles"]
            
            head=[]
            day=["first","second","third","fourth","fifth","sixth"]
            for ar in articles:
                head.append(ar["title"])
            for i in range (len(day)):
                self.respond(f" Today's {day[i]}  news is : {head[i]}")




        elif 'tell me joke' in string or 'joke'in string:
            joke=pyjokes.get_joke()
            self.respond(joke)



        elif 'wikipedia' in string:
            self.respond('Getting Information From Wikipedia')
            string=string.replace("wikipedia","")
            result=wikipedia.summary(string,sentences=2)
            self.respond(result)

        elif'play music' in string:
            self.respond('Playing Music')
            music_dir='G:\Music\_Evergreen'
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            #print(songs)
            os.startfile(os.path.join(music_dir,rd))

       
        elif'temperature' in string:
            self.respond("Getting the Temperature")
            search ="Temperature in phagwara"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            self.respond(f"The Temperature Outside is {temp}")

        elif'cancel chrome'in string:
            self.respond("Closing Chrome Sir")
            os.system("TASKKILL /F /im chrome.exe")


        elif'vs code'in string:
            self.respond("Opening Vs Code")
            codepath="C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codepath)

        elif'close code' in string:
            self.respond('Closing Sir')
            os.system("TASKKILL /F /im devenv.exe") 

        elif'c compiler'in string:
            self.respond("Opening C Compiler")
            codepath="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codepath)

        elif'close compiler' in string:
            self.respond('Closing Sir')
            os.system("TASKKILL /F /im devcpp.exe")   

        elif'telegram'in string:
            self.respond("Opening Telegram")
            codepath="C:\\Users\\home\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(codepath) 

        elif'close' in string:
            self.respond('Closing Sir')
            os.system("TASKKILL /F /im Telegram.exe")          

        elif'take screenshot' in string:
            self.respond('Taking Screenshot ')
            sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{string}.jpg")
            self.respond('Done Sir')

        
        elif'math class' in string:
            from automation import classMaths
            name=string.replace("maths ","")
            name=name.replace("class","")
            self.respond('Joining Maths Class Sir')
            classMaths('subject')

        elif'english class' in string:
            from automation import classEnglish
            name=string.replace("english","")
            name=name.replace("class","")            
            self.respond('Joining English Class Sir')
            classEnglish('subject')

        elif'science class' in string:
            from automation import classScience
            name=string.replace("Science ","")
            name=name.replace("class","")
            self.respond('Joining Science Class Sir')
            classScience('subject')
        
        
        
        elif'message' in string:
            name=string.replace("WhatsApp ","")
            name=name.replace("send","")
            name=name.replace("message","")
            Name=str(name)
            self.respond(f"Sending Hello TO  {Name}")
            
            from automation import whatsappMsg
            whatsappMsg(Name,'msg')

        elif'call'in string:
            from automation import whatsappCall
            name=string.replace("call","")
            Name=str(name)
            self.respond(f'Calling {Name}')
            whatsappCall(Name)

        elif'show chat' in string:
            
            from automation import whatsappChat
            name=string.replace("show","")
            name=name.replace("chat","")
            Name=str(name)
            self.respond(f'Showing Chats With {Name}')
            whatsappChat(Name)

        elif'camera' in string:
            self.respond('Opening Camera Sir')
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif'click my photo' in string:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press('enter')
            pyautogui.sleep(3)
            self.respond("Smile")
            pyautogui.press("enter")

        elif'ms word'in string:
            
            pyautogui.press("super")
            pyautogui.typewrite("ms word")
            pyautogui.press('enter')
            pyautogui.sleep(4)
            pyautogui.press('enter')
            sleep(3)
            self.respond("MS Word Opened Sir ")

        elif'ms excel'in string:
            
            pyautogui.press("super")
            pyautogui.typewrite("excel")
            pyautogui.press('enter')
            pyautogui.sleep(4)
            pyautogui.press('enter')
            sleep(3)
            self.respond("MS Excel Opened Sir ")


        elif'powerpoint'in string:
            
            pyautogui.press("super")
            pyautogui.typewrite("power point")
            pyautogui.press('enter')
            pyautogui.sleep(4)
            pyautogui.press('enter')
            sleep(3)
            self.respond("MS Power Point Opened Sir ")



        elif'mobile cam' in string:
            import urllib.request
            self.respond('Showing The Mobile cam Sir') 
            URL="http://192.168.18.17:8080/shot.jpg"
            while True:
                img_arr=np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img=cv2.imdecode(img_arr,-1)
                cv2.imshow('IPWebcam',img)
                q=cv2.waitKey(1)
                if q==ord("q"):
                    break;

            cv2.destroyAllWindows()


        elif'shutdown' in string:
            self.respond('Shutting Down The System Sir')
            os.system("shutdown /s /t 1")

        elif'restart' in string:
            self.respond('Restarting  The System Sir')
            os.system("shutdown /r /t 1")

        elif'logout' in string:
            self.respond('Logout The System Sir')
            os.system("shutdown -l")

        elif'facebook' in string:
            self.respond("Opening Facebook Sir")
            web.open('https://www.facebook.com/')

        elif'instagram' in string:
            self.respond("Opening Instagram Sir")
            web.open('https://www.instagram.com/')       

        elif'location' in string:
            self.respond('Getting the Location')
            web.open('https://www.google.com/maps/@31.2558448,75.6917338,16z')

        elif'game' in string:
            self.respond("Opening Snow Game Sir")
            codepath="C:\\Users\\home\\Desktop\\Voice_Assist-master\\SnoSnow.exe"
            os.startfile(codepath)

        elif 'bye' in string or 'exit' in string:
            name=self.name
            self.respond(f"Bye {name} Have a Nice Day . ")

            self.main_window.close()
            return False
        return True

    # VoiceEngine.VoiceSynth().synthesize_speech(VoiceEngine.TypeComm(), string, True)

    def respond(self, response):

        if self.voice.comms_object.comm_status():
            # Below condition shows that if there is a internet error and the synthesize_speech function returns false
            # then the internet status is set to false
            if not self.voice.synthesize_speech(response):
                self.main_window.switch_comm()
                self.main_window.signal_set_status.emit('Internet Error')
            else:
                self.main_window.signal_set_status.emit('Speaking...')
                self.main_window.signal_append_chatbot_history.emit(response)
                self.voice.speak()
                self.main_window.signal_set_status.emit('')
        else:
            self.main_window.signal_append_chatbot_history.emit(response)

    def run(self):
        while self.voice.comms_object.comm_status():

            self.main_window.signal_set_status.emit('Listening......')
            self.main_window.input_string = self.voice.listen()
            self.main_window.signal_set_status.emit('Thinking.......')
            if self.main_window.input_string == -1:
                self.respond('Didn\'t catch That , speak Again')
                continue
            if self.main_window.input_string == -2:
                self.main_window.switch_comm()
                self.signal_set_status.setText('Internet Error.Text Only')
                continue

            self.main_window.signal_append_user_history.emit(str(self.main_window.input_string))
            if not self.process(self.main_window.input_string):
                break


if __name__ == '__main__':
    # process('time', 1, 2, 3)
    pass
