def jerigonzo(string):
    aux = ""
    for letra in string:
        if letra in "aeiouAEIOU":
            aux += letra
            aux += "p"
        aux += letra
    
    return aux

if __name__ == "__main__":
    ingreso = str(input("Ingrese palabra o letra: "))
    palabra = jerigonzo (ingreso)
    print ("La Palabra Jerigonzo es: ", palabra)
    
    pass
         