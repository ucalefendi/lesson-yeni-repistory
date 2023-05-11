from bs4 import BeautifulSoup
import requests
import lxml


url = "https://www.imdb.com/chart/top/"

request = requests.get(url)
soup = BeautifulSoup(request.content, "lxml")

# print(soup)

top_250 = soup.find("tbody",attrs={"class":"lister-list"}).find_all('tr')
film_sira = 1

for film in top_250:
    adi = film.find("td",attrs={"class":"titleColumn"}).a.text
    yili = film.find("td",attrs={"class":"titleColumn"}).span.text
    puan = film.find("td",attrs={"class":"ratingColumn imdbRating"}).strong.get("title")

    print("film sira :", film_sira)
    print("film adi :", adi)
    print("film ili :", yili)
    print("film puan :", puan)

    film_sira +=1

