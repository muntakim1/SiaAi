import aiml
import pyttsx3 as pyttsx

import speech_recognition as sr

kernel = aiml.Kernel()
kernel.learn("botbrains\*.aiml")
kernel.saveBrain("siabrain.brn")

r = sr.Recognizer()
while 1:
    with sr.Microphone(device_index=1) as source:
        print('Say Something!')
        audio = r.listen(source)
        print(r.recognize_google(audio))
        print('Done!')

    try:
        text = r.recognize_google(audio)

        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 30)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        if text == "who are you" or text == "what is your name":
            engine.say("My name is Siaa")
        else:
            engine.say(kernel.respond(text))
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(e)
