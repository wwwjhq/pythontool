import requests
import sys

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1&lang=en"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            current = data['current_condition'][0]
            temp = current['temp_C']
            humidity = current['humidity']
            windspeed = current['windspeedKmph']
            weather_desc = current['weatherDesc'][0]['value']
            print(f"🌍 {city}: {weather_desc}, 温度 {temp}°C, 湿度 {humidity}%, 风速 {windspeed} km/h")
        else:
            print("查询失败")
    except Exception as e:
        print(f"错误：{e}")

if __name__ == "__main__":
    city = input("请输入城市名（英文）：").strip()
    get_weather(city)