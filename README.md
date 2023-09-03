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
  The user enters the book title only using which the parser finds relevant results. This version of search is less accurate than the second version as it can provide results of many authors having that title words in their books.
  </br>

- ### Option 2: search using author name and book title
  User provides the book title and the author's name. The book title opens the search page with that title name and the        author name is matched with the results to find all displayed results of that author. This is more precise as it can narrow down the book to that of a particular author.</br>

## Working Executable Images
<p align = "center">
  <img src="https://github.com/daimbk/bookstore-notif/assets/51926730/44104576-258b-43a5-8138-6108cea42b2b" width="400" height="300"/>
  </br></br>
  <img src="https://github.com/daimbk/bookstore-notif/assets/51926730/95c330ed-224c-4fb6-baa7-73dd83fa94f4" width="800" height="300"/>
</p>
