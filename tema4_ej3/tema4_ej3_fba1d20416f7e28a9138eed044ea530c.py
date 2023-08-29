def jerigonzo(string):
    cadena = ""
    for i in range(len(string)):
        x = string[i].upper()
        if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
            cadena += string[i]
            cadena += "p"
            cadena += string[i]
        else:
            cadena += string[i]
    return cadena    