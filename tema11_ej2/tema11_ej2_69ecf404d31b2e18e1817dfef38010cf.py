def validar_expresion(expresion):
    contador = 0
    contador_n = 0
    for digito in expresion:
        if digito.isnumeric() == False:
            contador = contador + 1
        else:
            contador_n = contador_n + 1
    if contador != 1:
        return False
    if contador_n == 1:
        return False
    else:
        return True



if __name__ == "__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           