import speech_recognition as sr
from Body.speak import Speak
def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():

    while True:

        query = Listen().lower()

        if "wake up" in query:
            return "True-Mic"
        
        else:
            pass
WakeupDetected()
Speak("Hello sir")