import requests

my_api_key = "4c95069a20a287d16e8deee1adac111f"
my_city = "San Franscisco"
url = f"https://api.openweathermap.org/data/2.5/weather?q={my_city}&appid={my_api_key}"

response = requests.get(url)
#print(response)
if response.status_code == 200:
    weather_data = response.json()
    info=weather_data['main']['temp']
    c=(int(info)-273)
    print(f"Temperature in your city {my_city}:{c}")
    print(f"Weather in your city {my_city} is: {weather_data['weather'][0]['description']}")
else:
    print("Failed to fetch weather data of your city.")