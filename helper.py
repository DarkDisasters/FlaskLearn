def is_isbn_or_key(word):
    """
        q:普通关键字 isbn
        page
        word参数接收 q
    """
    # isbn isbn13 13个0到9的数字组成
    # idbn10 10个0到9数组组成，含有一些 ' - '
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():    #要判断q中是不是全是数字
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key