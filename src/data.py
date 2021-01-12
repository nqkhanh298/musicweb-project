import requests
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup

from controller import getID

def crawlChart ():
# connect 
    url = "https://www.nhaccuatui.com/bai-hat/top-20.au-my.html"
    conn = urlopen(url)
    raw_data = conn.read()
    page_content = raw_data.decode("utf8")

    # f = open("zingchart.html", "wb")
    # f.write(raw_data)
    # f.close()

    # Extra ROI
    soup = BeautifulSoup(page_content, "html.parser")
    list_chart_page = soup.find("div", "list_chart_page")
    resource_slide = list_chart_page.find("div", "box_resource_slide")
    list_chart_slide = resource_slide.ul

    # Extra data
    list_chart_info = [] 

    list_chart = list_chart_slide.find_all("li")

    for chart in list_chart:
        rank_field = chart.find("span", "chart_tw")
        rank = rank_field.string
        info_field = chart.find("div", "box_info_field")
        link = info_field.a["href"]
        avatar = info_field.a.img["src"]
        idSong = getID(link)
        title = info_field.h3.a.string
        singer_list_a = info_field.h4.find_all("a")
        singer_list = []
        for a in singer_list_a:
            singer = a.string
            singer_list.append(singer)

        chart_info = {
            "rank": rank,
            "title": title,
            "id": idSong,
            "link": link,
            "singers": singer_list,
            "avatar": avatar
        }
        
        list_chart_info.append(chart_info)

    return list_chart_info

def dataBaseSinger(singer):
    # connect 
    url = "https://www.nhaccuatui.com/nghe-si-" + singer + ".html"
    conn = urlopen(url)
    raw_data = conn.read()
    page_content = raw_data.decode("utf8")

    # Extra ROI
    soup = BeautifulSoup(page_content, "html.parser")
    listGenre = soup.find("ul", "listGenre")

    # Extra data
    recommend_info = {}
    list_recommend_info = []
    li = listGenre.find_all("li")
    for data in li:
        info_song = data.find("div", "info_song")
        link = info_song.a["href"]
        avatar = info_song.a.img["src"]
        idSong = getID(link)
        title = info_song.a["title"]

        recommend_info = {
            "title": title,
            "link": link,
            "id": idSong,
            "avatar": avatar,
        }

        list_recommend_info.append(recommend_info)

    return list_recommend_info

def getAllSong (url):
    # connect 
    # url = "https://www.nhaccuatui.com/bai-hat/pop-moi.2.html"
    url = url
    conn = urlopen(url)
    raw_data = conn.read()
    page_content = raw_data.decode("utf8")    

    soup = BeautifulSoup(page_content, "html.parser")
    ul = soup.find("ul", "listGenre")
    li = ul.find_all("li")

    list_song_info = []
    for item in li:
        info_song = item.find("div", "info_song")
        link = info_song.a["href"]
        idSong = getID(link)
        title = info_song.a["title"]
        avatar = info_song.a.img["src"]

        song_info = {
            "title": title,
            "id": idSong,
            "link": link,
            "avatar": avatar
        }

        list_song_info.append(song_info)
    
    # print(list_song_info)

    return list_song_info

