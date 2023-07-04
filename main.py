import scrape


def func_options():
    print("\t1. Search using book title.\n\t2. Search using author name and book title (Improved Search).")
    option = int(input("Enter option number: "))

    while option not in (1, 2):
        option = int(input("Please enter correct option. 1 or 2: "))

    if option == 1:
        # call scraping script to check book availability using book title
        scrape.check_book()

    else:
        # search using author name and book title
        scrape.check_book_author()


def check_again():
    exit = False

    while not exit:
        # check if user wants to check another book
        option = input("\nCheck another book? (Y/N): ").upper()
        while option not in ('Y', 'N', 'y', 'n'):
            option = input("Please enter correct option. Y or N: ").upper()

        if option == 'Y' or option == 'y':
            func_options()
        else:
            exit = True


if __name__ == '__main__':
    print("Welcome to Book Availability Checker")
    option = func_options()

    check_again()
