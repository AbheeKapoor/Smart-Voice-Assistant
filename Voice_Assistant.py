import os
import speech_recognition as sr




def takecommand():
    command=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening......")
        command.pause_threshold=1
        audio=command.listen(source)

        try:
            print("Recognizing......")
            query=command.recognize_google(audio,language='en-in')
            print(f"You said:{query}")

        except:
            return"none"

        return query.lower()

while True:
    wake_Up=takecommand()
 

    if'start' in wake_Up:
        os.startfile('C:\\Users\\home\\Desktop\\Voice_Assist-master\\app.py')

    else:
        print("nothing")