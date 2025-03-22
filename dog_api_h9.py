import requests
dog_url="https://dog.ceo/api/breeds/image/random"
response=requests.get(dog_url)
if response.status_code==200:
    print(response.json())
else:
    print("NOT AVILABLE")