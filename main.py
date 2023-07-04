import scrape

if __name__ == '__main__':
    # call scraping script to check book availability
    scrape.check_book()
    exit = False

    while not exit:
        # check if user wants to check another book
        option = input("\nCheck another book? (Y/N): ").upper()
        while option not in ('Y', 'N'):
            option = input("Please enter correct option. Y or N: ").upper()

        if option == 'Y':
            scrape.check_book()
        else:
            exit = True
