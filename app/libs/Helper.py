# 开发时间： 2022/3/26 $ 23:41


def is_isbn_or_key(word):
    """
        :param word: 普通关键字 isbn
    """
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些 ' - '
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key