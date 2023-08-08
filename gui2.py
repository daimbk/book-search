import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, QWidget, QDesktopWidget
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QFont, QColor
import webbrowser
from scrape import func_options

header_style = 'font: 22pt "Exo"; font-weight: bold;'
bg_color = '#181E30'
fg_color = '#EEEEEE'
fg_color1 = '#000000'
button_color = '#FFD700'
font_style = 'font: 12pt "Andante"; font-weight: bold;'
font_style1 = 'font: 18pt "Exo"; font-weight: bold;'

rounded_button_style = (
            f"background-color: {button_color}; color: {fg_color1}; {font_style}"
            "border-radius: 20px;"
            "padding: 10px 20px;"
        )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BLookup")
        self.setGeometry(0, 0, 400, 300) 
        self.setFixedSize(self.size())

        # Set the background color for the entire window
        self.setStyleSheet(f"background-color: {bg_color};")
        self.init_ui()
        
        self.result_window = None

    def init_ui(self):
        layout = QVBoxLayout()

        lw_l1 = QLabel("WELCOME NERD")
        lw_l1.setStyleSheet(f"color: {fg_color}; {header_style}")
        lw_l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(lw_l1, alignment=Qt.AlignCenter)

        placeholders = ["Book Title", "Author Name"]
        self.entry_boxes = []  # Store entry boxes in a list

        for p in placeholders:

            entry_box = QLineEdit()
            entry_box_style = (
                f"background-color: {fg_color}; color: {fg_color1}; {font_style}"
                "border-radius: 15px;"
                "padding: 5px;"
            )
            entry_box.setStyleSheet(entry_box_style)
            entry_box.setPlaceholderText(f"{p}...")
            layout.addWidget(entry_box, alignment=Qt.AlignCenter)
            self.entry_boxes.append(entry_box)  # Add the entry box to the list

        search = QPushButton("Search")
        search.setStyleSheet(rounded_button_style)
        search.clicked.connect(self.click)
        layout.addWidget(search, alignment=Qt.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def click(self):
        book_name = self.entry_boxes[0].text().strip()
        author_name = self.entry_boxes[1].text().strip()

        results = func_options(book_name, author_name)
    
        if results:
            self.result_window = ResultWindow(results)  # Create the ResultWindow instance with valid results
            self.result_window.show()
            self.hide()


class ResultWindow(QMainWindow):
    def __init__(self, results):
        super().__init__()

        self.setWindowTitle("Search Results")
        self.setGeometry(0, 0, 1500, 970)  # Set initial size, will be resized later

        # Set the background color for the entire window
        self.setStyleSheet("background-color: #181E30;")

        self.init_ui(results)

    def init_ui(self, results):
        layout = QVBoxLayout()

        header_layout = QHBoxLayout()

        back_button = QPushButton("<-")
        back_button.setStyleSheet(rounded_button_style)
        back_button.clicked.connect(self.back)
        header_layout.addWidget(back_button, alignment=Qt.AlignLeft)

        result_label = QLabel("Search Results")
        result_label.setStyleSheet(f"color: {fg_color}; {header_style}")
        header_layout.addWidget(result_label, alignment=Qt.AlignCenter)

        placeholder_label = QLabel("")
        header_layout.addWidget(placeholder_label, alignment=Qt.AlignRight)

        layout.addLayout(header_layout)

        # Add a spacer widget to create some space between the label and the table
        spacer = QWidget()
        spacer.setFixedSize(10, 20)  # Adjust the size as needed
        layout.addWidget(spacer)

        self.table = QTableWidget(len(results), 5)  # Create a 5-column table
        self.table.setHorizontalHeaderLabels(["SR", "Link", "Title", "Author", "Price"])  # Set column headers
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Set resizing
        self.table.verticalHeader().setVisible(False)  # Hide vertical header

        for col in range(self.table.columnCount()):
            header_item = self.table.horizontalHeaderItem(col)
            if header_item:
                header_item.setFlags(Qt.NoItemFlags)

        # Set font and color for column headers
        header_font = QFont("Exo", 18, QFont.Bold)
        self.table.horizontalHeader().setFont(header_font)
        self.table.horizontalHeader().setStyleSheet(f"background-color: {bg_color}; color: black;")

        # Set font and color for cell entries
        cell_font = QFont("Exo", 18)
        cell_font.setBold(False)  # Make cell entries not bold
        self.table.setFont(cell_font)
        self.table.setStyleSheet(f"color: white; background-color: {bg_color};")  # Set table background color
        
        for row, result in enumerate(results):
            sr_item = QTableWidgetItem(str(row + 1))

            link_item = QTableWidgetItem("⧉")
            link_item.setBackground(QColor(f"{button_color}"))
            link_item.setForeground(QColor(f"{fg_color1}"))
            link_item.setData(Qt.UserRole, result["Link"])

            book_item = QTableWidgetItem(f" {result['Title']} ")
            author_item = QTableWidgetItem(f" {result['Author']} ")
            price_item = QTableWidgetItem(f" {result['Price']} ")

            sr_item.setFlags(Qt.NoItemFlags)
            book_item.setFlags(Qt.NoItemFlags)
            author_item.setFlags(Qt.NoItemFlags)
            price_item.setFlags(Qt.NoItemFlags)
            
            # Make the cells under Link column clickable
            link_item.setFlags(Qt.ItemIsEnabled)

            # Set alignment for cell entries to center
            sr_item.setTextAlignment(Qt.AlignCenter)
            link_item.setTextAlignment(Qt.AlignCenter)
            book_item.setTextAlignment(Qt.AlignCenter)
            author_item.setTextAlignment(Qt.AlignCenter)
            #price_item.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(row, 0, sr_item)
            self.table.setItem(row, 1, link_item)
            self.table.setItem(row, 2, book_item)
            self.table.setItem(row, 3, author_item)
            self.table.setItem(row, 4, price_item)

        # Connect the cell clicked signal to the handle_cell_click method
        self.table.cellClicked.connect(self.handle_cell_click)

        # Allow vertical scrollbar even when content does not exceed available space
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        layout.addWidget(self.table)

        for row in range(self.table.rowCount()):
            # Set the row height to 50 pixels
            self.table.setRowHeight(row, 50)

        new_width = self.table.horizontalHeader().length() + 45
        new_height = self.table.verticalHeader().length() + result_label.sizeHint().height() + 105
        
        # Set the new width and height for the window
        self.resize(new_width, new_height)
        self.setFixedSize(self.size())

        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)


    def back(self):
        main_window.show()
        self.hide()


    def handle_cell_click(self, row, col):    
        if col == 1:  # Check if the clicked cell is under the "Link" column
            item = self.table.item(row, col)
            link = item.data(Qt.UserRole)  # Retrieve the stored link from user data
            webbrowser.open(link)    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
