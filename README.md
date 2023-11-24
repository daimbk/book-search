# Book Availability Checker using Web Scraping

The Book Availability Checker is an application built using React for the frontend and Flask for the backend. It allows users to check the availability of books on the [Readings](https://www.readings.com.pk/) bookstore website through web scraping.

## Features

- **Search Options:**
  - Users can search for book availability using either the book title or both the book title and author's name.
  - Two search options are available for more flexibility.

- **Result Information:**
  - The application displays result windows for each book containing Book Title, Author, Price, Availability, and the link to the storepage for that item.

## Frontend (React)

The frontend of the application is developed using React.

## Backend (Flask)

The backend of the application is built using Flask, a lightweight Python web framework. It handles the web scraping logic and communicates with the frontend. Key aspects include:

- **Web Scraping:**
  - Utilizes BeautifulSoup for parsing HTML and extracting relevant information from the Readings website.
  - Checks the availability status of each book.

- **Flask API:**
  - Exposes a `/search` endpoint for handling search requests from the React frontend.
  - Sends back search results in real-time as each book's availability is determined.

## How to Run

1. **Install Dependencies:**
   - In the root directory, run `npm install` to install React dependencies.
   - In the `backend` directory, install Flask dependencies with `pip install -r requirements.txt`.

2. **Run the Applications:**
   - Start the React app by running `npm start` in the `root` directory.
   - Run the Flask backend with `python app.py` in the `backend` directory.

3. **Access the App:**
   - Open your browser and go to `http://localhost:3000` to use the Book Availability Checker.

Feel free to explore the application, search for your favorite books, and check their availability in real-time!
