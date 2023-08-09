# Book Availability Checker using Web Scraping

The program created using python scripts gets the title or title/author from the user and scrapes the bookstore website [Readings](https://www.readings.com.pk/) to check if it is available.
</br>
The website houses items in 3 states which the scraper checks and conveys accordingly:
- Available
- Out of Stock
- Pre-Order

## Dependencies

- ### BeautifulSoup:
  Installation:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install beautifulsoup4`
  
  BeautifulSoup is an html parser which is used to find specific html and extract the data in the tags.
  </br>
  
  ```python
  # declare BeautifulSoup object passing webpage html to it
  soup = BeautifulSoup(html_content, "html.parser")

  # finding required elements such as book title and price
  title = soup.find('div', class_='books_detail_page_left_colum_author_name').find('h5').contents[0].strip()
  price = soup.find('div', class_='books_our_price').find('span', class_='linethrough').find_next_sibling('span')
  ```

- ### PyQt5:
  Installation:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install PyQt5`
  
  It is used to make the GUI of the program.

## Search Options

- ### Option 1: search using book title only
  The user enters the book title only using which the parser finds relevent results. This version of search is less accurate than   the second option (explained further in option 2).
  </br>

- ### Option 2: search using author name and book title
  User provides the book title and the author's full name. The book title opens the search page with that title name and the        author name is matched with the results to find all displayed results of that author. This is more precise as it can find         results with unique names such as:</br>
  + Special Editions
  + Hardcover Edition etc.

## Working Executable Images
<p align = "center">
  <img src="https://github.com/daimbk/bookstore-notif/assets/51926730/a0fb901e-5f5e-4a79-953a-069d0c52ef1f" width="750" height="350" border="15"/>
  </br>
  <img src="https://github.com/daimbk/bookstore-notif/assets/51926730/68e735de-8c44-45c6-9d35-b470855b68eb" width="750" height="350" border="15"/>
</p>
