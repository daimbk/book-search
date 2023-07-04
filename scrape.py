from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# get user input of book to check
book = input("Enter book name: ").title()
author = input("Enter author's full name: ").lower()

# result page upon searching
url = f'https://readings.com.pk/Pages/searchresult.aspx?Keyword={book}'

options = Options()
options.add_argument("-headless")  # run Firefox in headless mode
service = Service("geckodriver-v0.33.0-win64")  # path to gecko webdriver
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)
# get page html
html_content = driver.page_source

# parse html with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

""" find and filter the list of results """
# find the relevant <div> elements and extract information
div_elements = soup.find_all(
    'div', class_='product_detail_page_left_colum_author_name')

book_links = []
book_author = ""
for div_element in div_elements:
    link = div_element.find('h5').find('a')['href']  # link to book page
    book_author = div_element.find('h6').text.strip()  # name of author

    if book_author == author:
        book_links.append(link)

print(book_links)

# print the current URL to verify if the search was successful
# print(driver.current_url)

driver.quit()
