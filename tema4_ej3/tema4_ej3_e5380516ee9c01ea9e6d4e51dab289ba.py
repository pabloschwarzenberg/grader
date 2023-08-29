def jerigonzo(string):
    jerigonzo_texto = ""
    for char in string:
        if char.lower() in "aeiouáéíóú":
            jerigonzo_texto += char + "p" + char.lower()
        else:
            jerigonzo_texto += char
    return jerigonzo_texto

