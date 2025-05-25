from bs4 import BeautifulSoup
import requests
response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all(class_="sc-142c02c-0 lmjbLF")
    # print(soup_list)
    res = soup_list[0]
    print(res.text)
    print(type(res.text))