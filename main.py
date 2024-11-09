# --------------------------- IMPORTS ---------------------------
import requests
from bs4 import BeautifulSoup

# --------------------------- REQUESTS/SOUP ---------------------------
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Fetch the webpage
response = requests.get(URL)
response.raise_for_status()
web_page = response.text

# Parse the content
soup = BeautifulSoup(web_page, "html.parser")

# --------------------------- SCRAPING ---------------------------
# Extract movie titles
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]  # Reversing the list

# Writing to file
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")