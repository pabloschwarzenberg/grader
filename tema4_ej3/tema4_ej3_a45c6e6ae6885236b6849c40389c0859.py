
def jerigonzo(string):
    traducido = ""
    for letra in string:
        traducido += letra
        if letra.lower() in "aeiou":
            traducido += "p" + letra
    return traducido
   

if __name__ == "__main__":
    pass
         