import requests

from bs4 import BeautifulSoup 
url = "https://coinmarketcap.com"
myresponse =requests.get(url)

if myresponse.status_code == 200:

    soup = BeautifulSoup(myresponse.text, 'html.parser')

    coinss = soup.find_all('a', class_='cmc-link')

    for coin in coinss:

        print(coin.text)
else:
    print(f"Failed to fetch the webpage. Status code:(myresponse.status_code)")