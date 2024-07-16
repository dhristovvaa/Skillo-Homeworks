#Problem 0

import requests

def fetch_http_cat_image(status_code):
    url = f"https://http.cat/{status_code}"

    try:

        response = requests.get(url)


        response.raise_for_status()


        print(f"Response status code: {response.status_code}")
        print(f"Response content type: {response.headers['Content-Type']}")


        with open(f"http_cat_{status_code}.jpg", "wb") as f:
            f.write(response.content)

        print(f"Image saved as http_cat_{status_code}.jpg")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")


status_code = input("Enter the HTTP status code: ")


fetch_http_cat_image(status_code)


#Problem 1
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


date_input = input("Enter the date (YYYY-MM-DD): ")
city = "San Francisco"


forecast_date = datetime.strptime(date_input, "%Y-%m-%d")


latitude = 37.7749
longitude = -122.4194


start_date = forecast_date.strftime("%Y-%m-%d")
end_date = (forecast_date + timedelta(days=1)).strftime("%Y-%m-%d")


url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&start_date={start_date}&end_date={end_date}&timezone=auto"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()


    times = data["hourly"]["time"]
    temperatures = data["hourly"]["temperature_2m"]


    df = pd.DataFrame({"Time": times, "Temperature": temperatures})


    df['Time'] = pd.to_datetime(df['Time'])

   
    sns.set(style="darkgrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x="Time", y="Temperature", marker="o")

    plt.title(f"Hourly Temperature Forecast for {city} on {forecast_date.strftime('%Y-%m-%d')}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print("Failed to retrieve data:", response.status_code)
