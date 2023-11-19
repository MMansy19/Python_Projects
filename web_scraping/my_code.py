# (0)import Required Libraries:
import requests
from bs4 import BeautifulSoup


# (1)Make HTTP Requests:
# Use the requests library to fetch the HTML content of the web page.
response= requests.get("https://books.toscrape.com/")

# (2)Parse HTML:
# Use a HTML parser like BeautifulSoup or  to extract information from the HTML content.

soup = BeautifulSoup(response.content, 'html.parser')
books=soup.findAll("article")
for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    price = soup.select_one("article > div.product_price > p")  
    print("Book title: "+ title +", rating: " + rating + ", price: " + (price.text)) 
    
    #  article > div.product_price > p.price_color")