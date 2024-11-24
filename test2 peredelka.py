print("A text")
from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.quotegarden.com/mind.html")
soup = BeautifulSoup(response.text, features="html.parser")
coins = [soup.find_all('p', "class": "left")]
file = open("coins,txt", 'w')
for i in range(0, len(coins[0])):
    print(f"{coins[0][i].text} {coins[1][i].text} {coins[2][i].text}")
    file.write(f"{coins[0][i].text} {coins[1][i].text}\n")

file.close()
