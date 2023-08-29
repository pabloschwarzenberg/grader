def jerigonzo(string):
    contador = 0
    while contador <= len(string):
        if string[contador] == "a" or string[contador] == "e" or string[contador] == "i" or string[contador] == "o" or string[contador] == "u" :
            string = string.replace(string[contador], string[contador] + "p" + string[contador])
            contador += 1
        else:
            contador += 1
    return string
         