import csv
import requests
from bs4 import BeautifulSoup
import time
from random import randint

base_url = "https://www.goodreads.com/list/show/183940.Best_Books_of_2023?page="
num_pages = 5
filename = "best_books.csv"

with open(filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Author", "Rating"])

    for page_number in range(1, num_pages + 1):
        url = base_url + str(page_number)

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        book_items = soup.find_all("tr", itemtype="http://schema.org/Book")

        for item in book_items:
            title = item.find("a", class_="bookTitle").text.strip()
            author = item.find("a", class_="authorName").text.strip()
            rating = item.find("span", class_="minirating").text.strip()
            writer.writerow([title, author, rating])
            print(title, author, rating)

        sleep = randint(1, 2)
        time.sleep(sleep)

