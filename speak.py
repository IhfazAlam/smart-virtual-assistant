import pyttsx3
import pythoncom
import threading


def speak(text):

    def run():

        pythoncom.CoInitialize()

        engine = pyttsx3.init()

        engine.setProperty('rate', 170)

        engine.setProperty('volume', 1)

        engine.say(str(text))

        engine.runAndWait()

        engine.stop()

        pythoncom.CoUninitialize()

    threading.Thread(target=run).start()