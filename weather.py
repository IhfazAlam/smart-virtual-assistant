import requests


def Weather():

    api_key = "aef3278f0fed3869ad77350211332f50"

    city = "Dhaka"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    data = requests.get(url).json()

    if data.get("main"):

        temp = data["main"]["temp"]

        desc = data["weather"][0]["description"]

        return f"{temp}°C with {desc}"

    else:

        return "Weather not available"