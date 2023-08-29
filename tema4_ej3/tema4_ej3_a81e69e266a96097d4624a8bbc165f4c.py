def jerigonzo(string):
    traductor = ""
    ua = ["A", "E", "I", "O", "U","a", "e", "i", "u", "o"]
    for l in string:
        if l in ua:
            traductor += l
            # agregar p despues de la vocal
            traductor += "p"
            traductor += l
        else:
            traductor += l
    return traductor