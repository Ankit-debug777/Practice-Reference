''''News-Top headlines
new() function collects all the material. That is converted into audio and saved in the system. The default audio app launches and the news.mp3 file is read
pros-mp3 file is available even after running the function so it can be listened to afterwards. cons-takes some time to execute'''
'''speak() function executes in less time. con- would require to executethe function again if want to listen again'''
import requests
import json

# def news(str):
#     from gtts import gTTS
#     import os
#     language='en'
#     headlines = gTTS(text=str, lang=language, slow=False)
#     headlines.save("news.mp3")
#     os.system("news.mp3")

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    want = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=putkeyhere")
    uh = want.json()
    print(json.dumps(uh,indent=2))
    cont =""
    for obj in uh['articles']:
        cont=cont+ f"{obj['title']}. {obj['description']}"
    speak(cont)