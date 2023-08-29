def jerigonzo(string):
    cadena = ''
    for elem in string:
        cadena += elem
        if (elem.upper() == 'A' or elem.upper() == 'E' or elem.upper() == 'I' or elem.upper() == 'O' or elem.upper() =='U'):
            cadena += 'p' + elem
    string = cadena
    return string