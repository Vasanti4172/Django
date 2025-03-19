import requests
from bs4 import BeautifulSoup
url = "https://coinmarketcap.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
   # <a href="/currencies/bitcoin/" class="currency-name-container">Bitcoin</a>

    coinss = soup.find_all('a', class_='cmc-link')
    for coin in coinss:
        print(coin.text)
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    