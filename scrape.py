import requests
from bs4 import BeautifulSoup


def check_book(book):
    """search using only book title (cannot detect specific versions such as special editions)"""
    # get user input of book to check
    book = book.title()

    # result page upon searching
    url = f'https://readings.com.pk/Pages/searchresult.aspx?Keyword={book}'

    # fetch the web page content
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching data from the website.")
        return

    # parse html with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    """ find and filter the list of results """
    # find the relevant <div> elements and extract information
    div_elements = soup.find_all(
        'div', class_='product_detail_page_left_colum_author_name')

    book_links = {}
    book_author = ""
    for div_element in div_elements:
        title = div_element.find('h5').find(
            'a').text.strip().title()  # name of book
        link = div_element.find('h5').find('a')['href']  # link to book page
        book_author = div_element.find(
            'h6').text.strip().title()  # name of author

        if title == book:
            book_links[link] = book_author

    # exit if no book is found
    if len(book_links) == 0:
        print("No books of such name found.")
        return

    book_info = []
    # open result pages
    for page in book_links:
        print()  # newline
        url = "https://readings.com.pk" + f"{page}"
        # fetch the new page content
        response = requests.get(url)
        if response.status_code != 200:
            print("Error fetching data from the website.")
            continue

        # parse the new page with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # get book details
        title = soup.find('div', class_='books_detail_page_left_colum_author_name').find(
            'h5').contents[0].strip()
        price = soup.find('div', class_='books_our_price').find(
            'span', class_='linethrough').find_next_sibling('span')
        price = price.text.strip()

        # check if book is available
        availability_elements = soup.find_all(class_='book_availability')
        availability = ""
        if availability_elements:
            availability = "Available"

        else:
            # check if book is out of stock
            out_of_stock_elements = soup.find_all(class_='out_off_stock')
            if out_of_stock_elements:
                availability = "Out of Stock"

            # check if available for pre-order
            else:
                pre_order_elements = soup.find_all(class_='pree_order')
                if pre_order_elements:
                    availability = "Available for Pre-Order"

        book_dic = {"Title": title,
                    "Author": book_links[page],
                    "Price": price,
                    "Link": url,
                    "Availability": availability}

        book_info.append(book_dic)

    return book_info


def check_book_author(book, author):
    """search using book title and author (more precise)"""
    # get user input of book to check
    book = book.title()
    author = author.title()

    # result page upon searching
    url = f'https://readings.com.pk/Pages/searchresult.aspx?Keyword={book}'

    # fetch the web page content
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching data from the website.")
        return

    # parse html with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    """ find and filter the list of results """
    # find the relevant <div> elements and extract information
    div_elements = soup.find_all(
        'div', class_='product_detail_page_left_colum_author_name')

    book_links = {}
    book_author = ""
    for div_element in div_elements:
        title = div_element.find('h5').find(
            'a').text.strip().title()  # name of book
        link = div_element.find('h5').find('a')['href']  # link to book page
        book_author = div_element.find(
            'h6').text.strip().title()  # name of author

        if book_author == author:
            book_links[link] = book_author

    # exit if no book is found
    if len(book_links) == 0:
        print("No books of such name found.")
        return

    book_info = []

    # open result pages
    for page in book_links:
        print()  # newline
        url = "https://readings.com.pk" + f"{page}"

        # Fetch the new page content
        response = requests.get(url)

        if response.status_code != 200:
            print("Error fetching data from the website.")
            continue

        # parse the new page with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        # get book details
        title = soup.find('div', class_='books_detail_page_left_colum_author_name').find(
            'h5').contents[0].strip()
        price = soup.find('div', class_='books_our_price').find(
            'span', class_='linethrough').find_next_sibling('span')
        price = price.text.strip()

        # check if book is available
        availability_elements = soup.find_all(class_='book_availability')
        availability = ""
        if availability_elements:
            availability = "Available"

        else:
            # check if book is out of stock
            out_of_stock_elements = soup.find_all(class_='out_off_stock')
            if out_of_stock_elements:
                availability = "Out of Stock"

            # check if available for pre-order
            else:
                pre_order_elements = soup.find_all(class_='pree_order')
                if pre_order_elements:
                    availability = "Available for Pre-Order"

        book_dic = {"Title": title,
                    "Author": book_links[page],
                    "Price": price,
                    "Link": "https://readings.com.pk" + page,
                    "Availability": availability}

        book_info.append(book_dic)

    return book_info


def func_options(book, author):
    if author == "":
        # call scraping script to check book availability using book title
        return check_book(book.title())

    else:
        # search using author name and book title
        return check_book_author(book.title(), author.title())
