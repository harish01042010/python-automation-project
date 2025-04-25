import csv
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'http://books.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)

# Explicitly set the encoding to 'utf-8' to fix character issues
response.encoding = 'utf-8'

# Parse the content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the book containers
books = soup.find_all('article', class_='product_pod')

# Open the CSV file to save the data
with open('books.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['Title', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()  # Write the header row
    
    # Loop through each book and extract data
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text
        
        # Write the data to the CSV file
        writer.writerow({'Title': title, 'Price': price})

print("✅ Book data scraped and saved to books.csv")
