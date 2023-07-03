# same search using the search icon button press'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

# get user input of book to check
book = input("Enter book name: ")

url = "https://www.readings.com.pk/"

options = Options()
options.add_argument("-headless")  # run Firefox in headless mode
service = Service("geckodriver-v0.33.0-win64")  # path to gecko webdriver
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)

# find the search input element
search_input = driver.find_element(By.ID, "Search")

# clear the search input
search_input.clear()

# enter the book name
search_input.send_keys(book)

# press Enter to perform the search
search_input.send_keys(Keys.RETURN)

# print the current URL to verify if the search was successful
print(driver.current_url)

driver.quit()
