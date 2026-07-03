import webbrowser
from threading import Timer
from datetime import datetime
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "ceb9211f5d7b07e4a7a867768c13330f"
@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            weather = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].title(),
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "icon": data["weather"][0]["icon"],
                "feels_like": data["main"]["feels_like"],
                "pressure": data["main"]["pressure"],
                "visibility": data["visibility"] / 1000,
                "main": data["weather"][0]["main"],
                "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p"),
                "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p"),
            }

        else:
            error = "City not found!"

    return render_template(
    "index.html",
    weather=weather,
    error=error,
    current_date=current_date,
    current_time=current_time
)
current_date = datetime.now().strftime("%A, %d %B %Y")
current_time = datetime.now().strftime("%I:%M %p")

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=False)