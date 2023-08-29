def validar_expresion(expresion):
    lista = list(expresion)
    try:
        int(lista[0])
        int(lista[2])
        return True
    except:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           