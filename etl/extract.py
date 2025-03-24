import requests
import json 

api_url="https://api.openweathermap.org/data/2.5/weather"
params={
    "q":"New York",
    "appid":"91dbdebc1095e84899408b6a8873f2f2",
    "units":"metric"
}

def extract_data():
    response=requests.get(api_url,params=params)
    data=response.json()

    with open("weather_data.json","w")as f:
        json.dump(data,f,indent=4)
    print("Data Extracted successfully !")

if __name__ == "__main__":
    extract_data()