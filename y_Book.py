from httper import HTTP

class Book:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        # url = self.isbn_url.format(isbn)
        # url = Book.isbn_url.format(isbn)
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    def search_by_keyword(cls, keyword, count=15, start=0):
        # url = Book.keyword_url.format(url)
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result