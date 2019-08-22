import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("-----------------------------")
    print("Speak...")
    print("-----------------------------")
    audio = r.listen(source,phrase_time_limit=10)
    try:
        text = r.recognize_google(audio)
        print("You said :{}".format(text))
    except:
        print("Sorry could not recognize what you said")
