import requests

api_address="https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=00d05d292c3b4f3c83d438ea230c31b5"
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(5):
        ar.append("Number " + str(i+1) + "," + json_data["articles"][i]["title"]+".")
    return ar

arr=news()

# print(arr)