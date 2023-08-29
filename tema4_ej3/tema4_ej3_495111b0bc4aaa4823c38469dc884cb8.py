def jerigonzo(string):
    for l in string:
        if l == "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U":
            l = l + "p{}".format(l)
    return string
