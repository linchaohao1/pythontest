#通过指定分隔符对字符串进行切片，返回一个列表
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split()
    return words

#对列表进行排序，返回一个列表
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#移除列表的第一个元素，并打印
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

#移除列表的最后一个元素，并打印
def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)

#将字符串进行切片后，再进行排序，返回一个列表
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

#将字符串切片后，打印列表的第一个元素和最后个元素
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#将字符串切片并排序后，打印列表的第一个元素和最后个元素
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
