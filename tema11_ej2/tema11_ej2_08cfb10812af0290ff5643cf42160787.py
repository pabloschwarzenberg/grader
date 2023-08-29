def validar_expresion(expresion):
    lista_suma = expresion.split("+")
    lista_resta = expresion.split("-")
    if lista_suma[0].isnumeric() == True and lista_suma[1].isnumeric() == True:
        return True
    if lista_resta[0].isnumeric() == True and lista_resta[1].isnumeric() == True:
        return True
    else:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           