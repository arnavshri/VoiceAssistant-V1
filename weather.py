import requests

api_address='https://api.openweathermap.org/data/2.5/weather?q=Indore&appid=5dfaaa8b99bba580535c222e5af72124'
json_data = requests.get(api_address).json()

def temp():
    temprature= round(json_data["main"]["temp"]-273,1)
    return temprature

def des():
    description=json_data["weather"][0]["description"]
    return description

# print(temp())
# print(des())