# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from scrape import func_options

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.json
        book_name = data.get('bookName')
        author = data.get('author')

        result = func_options(book_name, author)
        return jsonify({'result': result})

    except Exception as e:
        print(f"Error: {str(e)}")  # Print the error in the terminal
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
