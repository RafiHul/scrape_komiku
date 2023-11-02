import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from fake_useragent import UserAgent


def search_name_manga(x):
    search_url = f"https://komikcast.net/?s={x}"

    response = requests.get(
        search_url, headers={"UserAgent": UserAgent().chrome}
    )

    response.raise_for_status()

    #with open("data_scrape.html",'w',encoding="utf-8") as file:
        #file.write(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    manga_find_titles = soup.find_all("div", {"class": "tt"})
    manga_find_links = soup.find_all("div", {"class": "animposx"})

    lists = []

    for title, link in zip(manga_find_titles, manga_find_links):
        title_text = title.find('h4').text
        link_a = link.find("a")
        url_text = link_a['href']  # Ini adalah bagian yang perlu diubah
        lists.append({"title": title_text, "url": url_text})


    return lists

def search_manga(b: str):
    request_url = f"{b}"
    
    response = requests.get(request_url, headers={"UserAgent": UserAgent().chrome})
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    eph_num_divs = soup.find_all("span", class_="lchx")

    episode_list = []
    for div in eph_num_divs:
        link_elements = div.find("a")
        chap_elements = div.find("chapter").text
        link_href = link_elements.get("href")
        episode_list.append({"chap": chap_elements, "url": link_href})
        
    return episode_list

manga_name = input("Masukkan Judul : ")
search_hasil = search_name_manga(manga_name)

if len(search_hasil) == 0:
    print("Judul Tidak Ditemukan")
else:
    for i, name in enumerate(search_hasil):
        ss = name['title']
        qq = name['url']
        print(f"{i+1}. {ss}, {qq}")

    manga_choice_inp = int(input("\nPilih Judul (pilih pakai nomer) : "))
    manga_choice = search_hasil[manga_choice_inp - 1]
    print(str(manga_choice['url']))
    chosen = search_manga(manga_choice['url'])
    for i, name in enumerate(chosen):
        ss = name['chap']
        qq = name['url']
        print(f"{i+1}. {ss}, {qq}")
    