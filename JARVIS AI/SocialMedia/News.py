import requests
import json
from Body.speak import Speak
from Body.Listen import MicExecution


def latestnews():
    api_dict ={"buisness":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=30c3c2d17e3e4d14be732c7528d009ec",
              "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=30c3c2d17e3e4d14be732c7528d009ec",
              "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=30c3c2d17e3e4d14be732c7528d009ec",
              "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=30c3c2d17e3e4d14be732c7528d009ec",
              "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=30c3c2d17e3e4d14be732c7528d009ec",
              "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=30c3c2d17e3e4d14be732c7528d009ec",
              "top news":"https://newsapi.org/v2/top-headlines?country=in&apiKey=30c3c2d17e3e4d14be732c7528d009ec"
              }
    content = None
    url = None
    Speak("Which field news do you want to sir,[business],[health],[science],[sports],[technology],[entertainment],or else[top news]")
    field = MicExecution()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
            if url is True:
                print("url not found")
    news = requests.get(url).text
    news = json.loads(news)
    Speak("Sir here is the first news.")
    
    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        Speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        
        print("[for continue news say continue ] and [for stop news say stop]")
        a = MicExecution()
        if str(a) == "continue"or"proceed":
            pass
        elif str(a) == "Stop":
            break
        Speak("Thats all")
        
            
            