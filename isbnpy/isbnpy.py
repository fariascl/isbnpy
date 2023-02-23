from requests import get
from bs4 import BeautifulSoup

BASE_URL: str = "https://isbnsearch.org/isbn"

class ISBNpy:
    def __init__(self, cookie):
        self.cookie = cookie

    def getdata(self, isbn):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
           'Cookie': self.cookie,
           'Referer': f'https://isbnsearch.org/isbn/{isbn}'
            }
        try:
            page = get(f"{BASE_URL}/{isbn}", headers=headers)
            if page.status_code == 403:
                return {'msg': 'cookie expired', 'status_code': 403}
            soup = BeautifulSoup(page.content, 'html.parser')
            res = soup.find('div', class_='bookinfo')
            title = res.find('h1').get_text()
            _p = []
            for p in res.find_all('p'):
                _p.append(p.get_text())

            isbn_13 = _p[0].split('ISBN-13: ')[1].strip()
            isbn_10 = _p[1].split('ISBN-10: ')[1].strip()
            author = _p[2].split('Author:')[1].strip()
            edition = _p[3].split('Edition:')[1].strip()
            binding = _p[4].split('Binding:')[1].strip()
            publisher = _p[5].split('Publisher:')[1].strip()
            published = _p[6].split('Published:')[1].strip()
            _json = {
                'title': title,
                'isbn_13': isbn_13,
                'isbn_10': isbn_10,
                'author': author,
                'edition': edition,
                'binding': binding,
                'publisher': publisher,
                'published': published,
                'status_code': 200
            }
            return _json
        except:
            return {'msg': 'isbn not found', 'status_code':404}
