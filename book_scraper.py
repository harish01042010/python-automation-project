import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "http://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# CSV file setup
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])  # Header

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        writer.writerow([title, price])

print("✅ Book data scraped and saved to books.csv")
