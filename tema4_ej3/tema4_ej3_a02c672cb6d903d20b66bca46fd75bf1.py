def jerigonzo(string):
    n_string = ""
    VOWELS = "aeiou"
    for c in string:
        if c in VOWELS.lower():
            n_string += c + "p" + c
        else:
            n_string += c
    return n_string