import requests
from bs4 import BeautifulSoup

def get_melon_chart():
    header_user = {
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }

    url = "https://www.melon.com/chart/index.htm"
    req = requests.get(url, headers=header_user)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    lst50 = soup.select(".lst50")
    lst100 = soup.select(".lst100")
    lst_top_100 = lst50 + lst100

    chart_data = []

    for i in lst_top_100:
        rank = i.select_one(".rank")
        song_title_element = i.select_one(".ellipsis.rank01 a")
        singer_element = i.select_one(".ellipsis.rank02 a")
        song_id_element = i.select_one(".ellipsis.rank03")
        if song_id_element is not None:
            song_id = song_id_element.get("value")
            info_url = f"https://www.melon.com/song/detail.htm?songId={song_id}"
        else:
            song_id = "N/A"
            info_url = f"https://www.melon.com/song/detail.htm?songId={song_id}"

        # 차트 데이터를 딕셔너리로 저장₩
        chart_data.append({
            "rank": rank,
            "song_title": song_title_element,
            "singer": singer_element,
            "info_url": info_url
        })

    return chart_data
