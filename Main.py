import requests

urls = []
mp3s = []


def make_list_of_podcast():
    def make_all_URLs():
        page_num = 0
        base = r"https://podbay.fm/api/episodes?podcastID=278981407&page="
        while True:
            podbay = requests.get(base + str(page_num))
            if len(podbay.text) < 16:
                return
            else:
                urls.append(base + str(page_num))
            page_num += 1

    def get_title_and_mp3_url(url):
        u = requests.get(url)
        for i in range(len(u.json()['episodes'])):
            mp3s.append([u.json()['episodes'][i]['enclosure']['url'], u.json()['episodes'][i]['title']])

    make_all_URLs()

    for url in urls:
        get_title_and_mp3_url(url)


def download(file):
    url = file[0]
    title = file[1].replace(":", "").replace("-", "").replace("?", "")

    r = requests.get(url)  # create HTTP response object

    # send a HTTP request to the server and save
    # the HTTP response in a response object called r
    with open(title + ".mp3", 'wb') as f:
        f.write(r.content)


def dl_all_podcast(path):
    make_list_of_podcast()
    download(mp3s[0])
    download(mp3s[1])


dl_all_podcast('t')