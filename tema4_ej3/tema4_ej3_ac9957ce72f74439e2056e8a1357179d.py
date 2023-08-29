def jerigonzo(string):
    new_string = ""

    for i in string:
        if i in ['a', 'e', 'i', 'o', 'u']:
            new_string += i + 'p' + i
        else:
            new_string += i
    return new_string


if __name__ == "__main__":
    pass
