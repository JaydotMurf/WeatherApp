# WeatherApp
# A simple weather app using python and the free Open Weather Map API

#!/usr/bin/bash

import tkinter as tk
import requests
import time

def getWeather():
    city = location.get()
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=485f3504221100228b7f770ac6f5a22e"
    json = requests.get(api).json()
    forecast = json['weather'][0]['description']
    temp = round(9 / 5 * (int(json['main']['temp'] - 273.5)) + 32, 1)
    humid = int(json['main']['humidity'])
    min = round(9 / 5 * (int(json['main']['temp_min'] - 273.5)) + 32, 1)
    max = round(9 / 5 * (int(json['main']['temp_max'] - 273.5)) + 32, 1)
    sun_rise = time.strftime("%I:%M:%S", time.gmtime(json['sys']['sunrise'] + 21600))
    sun_set = time.strftime("%I:%M:%S", time.gmtime(json['sys']['sunset'] + 21600))

    weather_data = f"{forecast}\n{temp}"
    weather_forecast = f"Min Temp: {min}\nMax Temp: {max}\nHumidity: {humid}\nSun Rise: {str(sun_rise)}\nSun Set: {str(sun_set)}"
    lbl1.config(text=weather_data)
    lbl2.config(text=weather_forecast)


window = tk.Tk()
window.geometry("600x500")
window.title("Weather App")

f = ("Times", 16, "bold")
t = ("Helvetica", 24, "bold")

location = tk.Entry(window, font=t, justify="center")
location.pack(pady=10)

# Enable user to type text no matter where the cursor is
location.focus()

search_btn = tk.Button(window, text="Search", font=t, command=getWeather)
search_btn.pack(pady=5)


lbl1 = tk.Label(window, font=t)
lbl1.pack(pady=5)
lbl2 = tk.Label(window, font=f)
lbl2.pack()

window.mainloop()
