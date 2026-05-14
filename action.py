import datetime
import webbrowser
import os
import speak
import weather


class VirtualAssistant:

    def __init__(self):

        pass

    # ---------------- SPEAK ---------------- #
    def speak_and_return(self, text):

        speak.speak(text)

        return text

    # ---------------- COMMANDS ---------------- #
    def get_name(self):

        return self.speak_and_return(
            "My name is Virtual Assistant"
        )

    def greet(self):

        return self.speak_and_return(
            "Hey sir, how can I help you?"
        )

    def how_are_you(self):

        return self.speak_and_return(
            "I am doing great these days sir"
        )

    def thanks(self):

        return self.speak_and_return(
            "It's my pleasure sir"
        )

    def good_morning(self):

        return self.speak_and_return(
            "Good morning sir"
        )

    def tell_time(self):

        now = datetime.datetime.now()

        time_text = f"The time is {now.hour}:{now.minute}"

        return self.speak_and_return(time_text)

    def shutdown(self):

        return self.speak_and_return(
            "Okay sir"
        )

    def play_music_online(self):

        webbrowser.open("https://gaana.com/")

        return self.speak_and_return(
            "Gaana is ready for you"
        )

    def open_google(self):

        webbrowser.open("https://google.com/")

        return self.speak_and_return(
            "Google opened"
        )

    def open_youtube(self):

        webbrowser.open("https://youtube.com/")

        return self.speak_and_return(
            "YouTube opened"
        )

    def get_weather(self):

        try:

            ans = weather.Weather()

            return self.speak_and_return(ans)

        except Exception:

            return self.speak_and_return(
                "Weather service not available"
            )

    def play_local_music(self):

        try:

            path = r"D:\music"

            songs = os.listdir(path)

            if not songs:

                return self.speak_and_return(
                    "No songs found"
                )

            os.startfile(
                os.path.join(path, songs[0])
            )

            return self.speak_and_return(
                "Playing songs"
            )

        except Exception:

            return self.speak_and_return(
                "Cannot access music folder"
            )

    # ---------------- MAIN ACTION ---------------- #
    def Action(self, send: str):

        data = send.lower().strip()

        print("User said:", data)

        # Greeting
        if any(word in data for word in ["hello", "hi", "hey"]):

            return self.greet()

        # Name
        elif "name" in data:

            return self.get_name()

        # How are you
        elif "how are you" in data:

            return self.how_are_you()

        # Thanks
        elif "thank" in data:

            return self.thanks()

        # Good morning
        elif "good morning" in data:

            return self.good_morning()

        # Time
        elif "time" in data:

            return self.tell_time()

        # Shutdown
        elif any(word in data for word in ["shutdown", "quit", "exit"]):

            return self.shutdown()

        # Music
        elif "play music" in data or "song" in data:

            return self.play_music_online()

        # Local music
        elif "music from my laptop" in data:

            return self.play_local_music()

        # Google
        elif "google" in data:

            return self.open_google()

        # YouTube
        elif "youtube" in data:

            return self.open_youtube()

        # Weather
        elif "weather" in data:

            return self.get_weather()

        # Unknown
        else:

            return self.speak_and_return(
                "I am not able to understand"
            )