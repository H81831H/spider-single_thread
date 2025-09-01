import requests,time,re
from bs4 import BeautifulSoup
import multiprocessing

def movie_catch(page):

    global url
    url = f"https://movie.douban.com/top250?start={page}&filter="
    
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}
    
    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        original = response.text
    else:
        print(f"Error,{response.status_code}")
    
    soup = BeautifulSoup(original,"lxml").find_all("span")

    return soup

def analysis(txt):

    pattern = '"title">\w*'

    txt = re.findall(pattern,str(txt))

    project = []

    for item in txt:
        item = item.lstrip('"title">')
        if item != '':
            project.append(item)

    return project


def catch_storage(project):

    with open('douban_TOP250movie.csv','a',encoding='utf-8') as file:

        for item in project:
            file.write(f"{item}\n")


if __name__ == '__main__':

    start = time.time()
    print("开始抓取")

    urls = []

    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    for i in range(0,250,25):
        soup = movie_catch(i)
        project = analysis(soup)
        catch_storage(project)
        #time.sleep(10)
    
    print(f"抓取完成，用时：{time.time() - start}")
