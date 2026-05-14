import speech_recognition as sr
import speak


def spech_to_text():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )

    try:

        print("Recognizing...")

        voice_data = r.recognize_google(audio)

        print("YOU SAID:", voice_data)

        return voice_data.lower()

    except sr.UnknownValueError:

        print("Could not understand")

        speak.speak("Sorry, I could not understand")

        return ""

    except sr.RequestError:

        print("Internet error")

        speak.speak("Internet connection error")

        return ""