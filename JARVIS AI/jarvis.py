from Body.Listen import MicExecution
from Brain.Qna import QuestionReplier
from Brain.AI_Brain import ReplyBrain
from Features.open import OpenExe
from Body.speak import Speak
#from Features.clap import Tester
import keyboard
import pywhatkit as pwt
from SocialMedia.Whatsapp import WhatsappMessage
from SocialMedia.Whatsapp import WhatsappCall
#from SocialMedia.Whatsapp import WhatsappChat
from SocialMedia.Whatsapp import WhatsappVideoCall
from SocialMedia.News import latestnews
from SocialMedia.Game import game_play
import datetime




print(">> Starting The Jarvis : Wait For Some Seconds.")

def MainExecution():
    Speak("Welcome back Sir?")
    Speak("I'm Jarvis, how are you feel today, I'am Ready to assist you sir")
    while True:
        info = MicExecution()
        info = str(info)
        valuereturn = OpenExe(info)
        if valuereturn==True:
            pass            

        elif len(info)<=1:
            pass
        elif"play" in info or "song" in info or "music" in info:
            name = info.replace("play"or"song"or"music","")
            pwt.playonyt(name)
            Speak(f"Sure Sir playing{name}")
            keyboard.press("spacebar")
            
        elif "hello" in info:
                Speak("Hello sir, how are you ?")
                if "i am fine" in info:
                    Speak("that's great, sir")
                elif "how are you" in info:
                    Speak("Perfect, sir")
                elif "thank you" in info:
                    Speak("you are welcome, sir")
        elif "time" in info:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            Speak(f"Sir, the time is {strTime}")
        elif "exit" in info:
            Speak("Going to sleep,sir")
            exit()
            
        elif "Whatsapp message" in info or "send Message" in info or "message" in info:
            name = info.replace("whatsapp message"or"send message"or "message","")
            Name = str(name)
            Speak(f"Whats the Message for {Name}")
            Msg = MicExecution()
            WhatsappMessage(Name, Msg)
        elif "call" in info or "calling" in info:
            name = info.replace("call" or "jarvis" or "calling","")
            Name = str(name)
            Speak(f"okay sir calling {Name}")
            WhatsappCall(Name)
        elif "show chat" in info or "chat" in info:
            name = info.replace("show chat"or"chat","")
            Name = str(name)
            WhatsappCall(Name)
        elif "video call" in info:
            name = info.replace("video call"or"jarvis","")
            Name = str(name)
            WhatsappVideoCall(Name)
        elif "news" in info:
            latestnews()
        elif "game" in info:
            Speak("I'am also feeling like playing the game with you")
            game_play()
        elif "song" in info or "music" in info:
            name = info.replace("play"or"song"or"music","")
            pwt.playonyt(name)
            Speak(f"Sure Sir playing{name}")
            keyboard.press("spacebar")
        elif "What is " in info or "where is" in info or "question" in info or "answer" in info:
            Reply = QuestionReplier(info)
            Speak(Reply)
        
        else:
            Reply = ReplyBrain(info)
            Speak(Reply)
#def ClapDetect():
    #Tester()
     
    #return True

#ClapDetect()         

MainExecution()    


