# Web Scraping: Book Information

This Python script demonstrates web scraping to extract book information from a sample book store website.

## Table of Contents

- [Dependencies](#dependencies)
- [Usage](#usage)
- [Description](#description)
- [Functionality](#functionality)
- [Example](#example)

## Dependencies

- `requests`: To make HTTP requests.
- `beautifulsoup4`: For HTML parsing.

## Usage

1. Install the required dependencies:

   ```bash
   pip install requests beautifulsoup4
   
##Description

The script fetches data from a sample book store website https://books.toscrape.com/.
It extracts information such as book title, rating, and price for each book.
The script uses the requests library to make HTTP requests and BeautifulSoup for HTML parsing.

##Functionality

make_request(url): Makes an HTTP request to the provided URL.
parse_html(response): Parses HTML content using BeautifulSoup.
extract_book_information(soup): Extracts book information such as title, rating, and price.

##Example

Running the script will print information about books available on the sample website.
