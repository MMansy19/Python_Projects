import requests
from bs4 import BeautifulSoup

def make_request(url):
    # Make HTTP Request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(f"Successfully fetched data from {url}")
        return response
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None

def parse_html(response):
    # Parse HTML using BeautifulSoup
    return BeautifulSoup(response.content, 'html.parser')

def extract_book_information(soup):
    # Extract Book Information
    books = soup.find_all("article")

    for book in books:
        # Extracting title
        title = book.h3.a["title"]

        # Extracting rating
        rating = book.p["class"][1]

        # Extracting price
        price_element = book.select_one("div.product_price p.price_color")
        price = price_element.text if price_element else "Price not available"

        # Print book information
        print(f"Book title: {title}, rating: {rating}, price: {price}")

def main():
    # Main function to orchestrate the script
    url = "https://books.toscrape.com/"

    # Make HTTP Request
    response = make_request(url)

    # Check if the request was successful
    if response:
        # Parse HTML
        soup = parse_html(response)

        # Extract Book Information and Print
        extract_book_information(soup)

if __name__ == "__main__":
    main()
