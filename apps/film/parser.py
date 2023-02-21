import requests, bs4


class TopCinema:
    # url = 'https://www.film.ru/a-z/movies/2022'
    url = 'https://me.anwap.tube/films/r2'

    def top(self):
        info = []
        page = requests.get(self.url)
        soup = bs4.BeautifulSoup(page.text, 'html.parser')
        data = soup.find_all('div', class_='my_razdel film')
        return data

# s = []
# data = TopCinema()
# for i in data.top():
#     film = i.find('a', class_='film_list_link')
#     s.append(str('https://www.film.ru/a-z/movies/2022'+film['href']))
# print(s)

# url = 'https://me.anwap.tube/films/r2'
# info = []
# page = requests.get(url)
# soup = bs4.BeautifulSoup(page.text, 'html.parser')
# data = soup.find_all('div', class_='my_razdel film')
# print(data)