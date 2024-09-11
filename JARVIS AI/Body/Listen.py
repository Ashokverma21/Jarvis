import speech_recognition as sr
from googletrans import Translator

# 1 - Listen: Hindi or English
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=8)  # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="hi")
        return query.lower()  # Convert to lowercase for consistency

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
        return ""

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# 2 - Translation
def TranslationHinToEng(text):
    if text:
        translate = Translator()
        result = translate.translate(text)
        data = result.text
        print(f"You: {data}.")
        return data
    else:
        return "No input detected."

# 3 - Connect
def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

if __name__ == "__main__":
    result = MicExecution()
    print("Translated Text:", result)
