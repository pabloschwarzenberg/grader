def jerigonzo(palabra):
    n_palabra = ""
    for c in palabra:
        if c == "a":
            n_palabra += c + "p" + c
        elif c == "e":
            n_palabra += c + "p" + c
        elif c == "i":
            n_palabra += c + "p" + c
        elif c == "o":
            n_palabra += c + "p" + c
        elif c == "u":
            n_palabra += c + "p" + c
        else: 
            n_palabra += c
    return n_palabra