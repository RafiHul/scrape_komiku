import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from fake_useragent import UserAgent


def search_name_manga(x):
    search_url = f"https://westmanga.info/?s={x}"

    response = requests.get(
        search_url, headers={"UserAgent": UserAgent().chrome}
    )

        # Is the response ok?
    response.raise_for_status()

        # parse with soup.
    soup = BeautifulSoup(response.text, "html.parser")
    manga_find_titles = soup.find_all("div", {"class": "tt"})
    manga_find_links = soup.find_all("div", {"class": "bsx"})

    lists = []

    for title, link in zip(manga_find_titles, manga_find_links):
        title_text = title.get_text(strip=True)
        link_a = link.find("a")
        url_text = link_a['href']
        lists.append({"title": title_text, "url": url_text})

    return lists

def search_episode_manga(episode_list):
    request_url = f"{episode_list}"
    
    response = requests.get(request_url, headers={"UserAgent": UserAgent().chrome})
    response.raise_for_status()

    eph_num_divs = soup.find_all("div", {"class": "eph-num"})

    episode_list = []
    for div in eph_num_divs:
        a_tag = div.find("a")
        href_text = a_tag['href']
        span_tag = div.find("span", {"class": "chapternum"})
        chapter_num_text = span_tag.get_text(strip=True)
        episode_list.append({"href": href_text, "chapternum": chapter_num_text})
        
    return episode_list

manga_name = input()
search_manga = search_name_manga(manga_name)

for i, name in enumerate(search_manga):
    ss = name['title']
    qq = name['url']
    print(f"{i+1}. {ss}, {qq}")