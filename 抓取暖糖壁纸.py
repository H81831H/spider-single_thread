import requests
import time
import re


def photos_fetch(page) ->list:
 
    url = f"https://www.nuantang.net/api.php?cid=360new&start={page}&count=10"
    
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"}
    
    response = requests.get(url,headers=headers,timeout=10)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error:{response.status_code}")

    photos_data = data["data"]["list"]
    
    global photos_url,photos_tag
    photos_url = []
    photos_tag = []

    for item in photos_data:
        photos_url.append(item["url"])
        photos_tag.append(item["tag"])

    #print(photos_tag)


def download():

    for index,item in enumerate(photos_url):

        img = requests.get(item).content

        with open(f'D:\\1my_code\\picture\\{photos_tag[index]}.jpg','wb') as file:
            file.write(img)
            print(f"download......{photos_tag[index]}")


if __name__ == '__main__':
    
    start = time.time()

    for i in range(21,31):
        photos_fetch(i)
        download()
        time.sleep(5)

    print('总耗时: %.2fs' % (time.time() - start))
