# Import Required Libraries
import requests
from bs4 import BeautifulSoup

# (1) Make HTTP Request:
# Use the requests library to fetch the HTML content of the web page.
url = "https://books.toscrape.com/"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(f"Successfully fetched data from {url}")
else:
    print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    exit()

# (2) Parse HTML:
# Use BeautifulSoup to extract information from the HTML content.
soup = BeautifulSoup(response.content, 'html.parser')

# (3) Extract Book Information:
# Find all book articles on the page and extract relevant information.
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

# End of the script
