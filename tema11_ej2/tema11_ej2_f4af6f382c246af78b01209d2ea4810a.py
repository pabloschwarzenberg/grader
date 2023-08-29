def validar_expresion(expresion):
    numeros = "1234567890"
    resultado = int(expresion)
    i = 0
    lista = string.split(resultado)
    for simbolo in lista:
        if simbolo in numeros == True:
            pass
        else:
            return False
    return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           