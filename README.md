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
  <img src="https://github.com/daimbk/bookstore-notif/assets/51926730/44104576-258b-43a5-8138-6108cea42b2b" width="400" height="300" border="15"/>
  </br></br>
  <img src="https://github.com/daimbk/bookstore-notif/assets/51926730/664df109-a024-4519-9057-cd90676a99d7" width="800" height="300" border="15"/>
</p>
