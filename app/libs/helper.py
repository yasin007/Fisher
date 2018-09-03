"""
create by 维尼的小熊 on 2018/8/30

"""
__autor__ = 'yasin'


def is_isbn_or_key(word):
    """

    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key
