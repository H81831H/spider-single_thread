import time
import requests
from bs4 import BeautifulSoup
import re

def main(page):

    url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-2-"+str(page)

    headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}

    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        original = response.text
    else:
        print(f"Error,{response.status_code}")

    soup = BeautifulSoup(original,'lxml')
    soup = str(soup.find_all("img"))

    pattern = '<img alt="\w*'
    txt = re.findall(pattern,soup)
    print(txt)

if __name__ == "__main__":
    for i in range(1,26):
        main(i)
        time.sleep(5)
