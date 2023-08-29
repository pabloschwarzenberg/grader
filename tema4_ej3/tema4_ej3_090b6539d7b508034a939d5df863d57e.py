def jerigonzo(string):
    hola = ""
    for letra in string:
        hola += letra
        if letra.lower() in "aeiou":
            hola += "p" + letra
            
    return hola 

if __name__ == "__main__":
    pass
         