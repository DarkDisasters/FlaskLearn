from flask import jsonify
from fisher import app
from y_Book import Book
from helper import is_isbn_or_key



@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q:普通关键字 isbn
        page
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        Book.search_by_isbn(q)
    else:
        result = Book.search_by_keyword(q)
    # dict序列化
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type':'application/json'}