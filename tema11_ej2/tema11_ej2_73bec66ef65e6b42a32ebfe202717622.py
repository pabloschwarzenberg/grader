def validar_expresion(expresion):
    if len(expresion) % 2 == 0:
        return False
    lista = []
    lista_numeros = ["0","1","2","3","4","5","6","7","8","9"]
    for i in expresion:
        lista.append(i)
    for i in range(len(lista)):
        if i % 2 == 0:
            if lista[i] not in lista_numeros:
                return False
        else:
            if lista[i] != "+" and lista[i] != "-":
                return False
    return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
