import tkinter as tk
from tkinter import messagebox
import requests

def get_weather_data(location_entry, temperature_label, humidity_label, wind_speed_label, pressure_label, precipitation_label):
    location = location_entry.get()
    if not location:
        messagebox.showinfo("Info", "Please enter a location.")
        return

    try:
        api_key = "e10c391fc9ef1b0181009e9bfce855cc"
        data = fetch_weather_data(location, api_key)

        temperature = f"Temperature: {data['main']['temp']}°C"
        humidity = f"Humidity: {data['main']['humidity']}%"
        wind_speed = f"Wind Speed: {data['wind']['speed']} km/h"
        pressure = f"Pressure: {data['main']['pressure']} hPa"
        precipitation = f"Precipitation: {data.get('rain', {'1h': 0}).get('1h', 0)}%"

        update_labels(temperature_label, humidity_label, wind_speed_label, pressure_label, precipitation_label,temperature, humidity, wind_speed, pressure, precipitation)

    except Exception as e:
        messagebox.showinfo("Info", f"An error occurred: {str(e)}")

def fetch_weather_data(location, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def update_labels(temperature_label, humidity_label, wind_speed_label, pressure_label, precipitation_label,temperature, humidity, wind_speed, pressure, precipitation):
    temperature_label.config(text=temperature)
    humidity_label.config(text=humidity)
    wind_speed_label.config(text=wind_speed)
    pressure_label.config(text=pressure)
    precipitation_label.config(text=precipitation)

def create_ui():
    root = tk.Tk()
    root.title("Weather Forecast App")
    root.geometry("500x500")

    location_label = tk.Label(root, text="Location:")
    location_label.grid(row=0, column=0)

    location_entry = tk.Entry(root)
    location_entry.grid(row=0, column=1)

    search_button = tk.Button(root, text="Search", command=lambda: get_weather_data(
        location_entry, temperature_label, humidity_label, wind_speed_label, pressure_label, precipitation_label
    ))
    search_button.grid(row=0, column=2)

    temperature_label = tk.Label(root, text="Temperature: ")
    temperature_label.grid(row=1, column=0)

    humidity_label = tk.Label(root, text="Humidity: ")
    humidity_label.grid(row=2, column=0)

    wind_speed_label = tk.Label(root, text="Wind Speed: ")
    wind_speed_label.grid(row=3, column=0)

    pressure_label = tk.Label(root, text="Pressure: ")
    pressure_label.grid(row=4, column=0)

    precipitation_label = tk.Label(root, text="Precipitation: ")
    precipitation_label.grid(row=5, column=0)

    root.mainloop()

create_ui()
