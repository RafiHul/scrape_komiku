import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

base_url = "https://komikcast.cz/"

x = input("masukkan nama manga : ").replace(" ","+")
qq = f"{base_url}?s={x}"
response = requests.get(qq,headers={"UserAgents": UserAgent().chrome})

soup = BeautifulSoup(response.text,"html.parser")
find_core_judul = soup.find_all("div",{"class":"list-update_item"})
store_manga = {}

for i in find_core_judul:
    title = i.find_next("h3",{"class":"title"}).getText(strip=True)
    links = i.find_next("a",{"class":"data-tooltip"}).get("href")
    chapter = i.find_next("div",{"class":"chapter"}).getText(strip=True)
    store_manga[title] = [links,chapter]

if not find_core_judul:
    print("tidak ada hasil")

print("\n".join([f"{i+1}. {k} ({store_manga[k][1]})" for i,k in enumerate(store_manga)]))

input_judul = int(input("Pilih Judul Menggunakan Angka : ")) - 1
key_manga_dipilih = list(store_manga.keys())[input_judul]
manga_dipilih_url = store_manga[key_manga_dipilih][0]

response = requests.get(manga_dipilih_url,headers={"UserAgents": UserAgent().chrome})

soup = BeautifulSoup(response.text,"html.parser")
find_core_chapter = soup.find_all("li",{"class":"komik_info-chapters-item"})
store_manga_chapter = {}
for i in find_core_chapter:
    chapter = i.find_next("a",{"class":"chapter-link-item"}).getText(strip=True).replace("\n"," ")
    chapter_url = i.find_next("a",{"class":"chapter-link-item"}).get("href")
    chapter_time = i.find_next("div",{"class":"chapter-link-time"}).getText(strip=True)

    store_manga_chapter[chapter] = [chapter_url,chapter_time]

print("\n".join([f"{n+1}. {i} ({store_manga_chapter[i][1]})\nLinks = {store_manga_chapter[i][0]}" for n,i in enumerate(store_manga_chapter)]))






