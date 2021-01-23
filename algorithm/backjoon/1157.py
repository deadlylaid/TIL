word = str(input()).lower()
types = set(word)


def count_char(word, types):
    max_number = 0
    char = 0
    is_dup = False

    for t in types:
        number = word.count(t)
        if max_number < number:
            char = t
            max_number = number
            is_dup = False
        elif max_number == number:
            is_dup = True

    if is_dup is True:
        return '?'
    else:
        return char.upper()

print(count_char(word, types))
