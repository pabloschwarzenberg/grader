def validar_expresion(expresion):
    lista=list(expresion)
    if len(expresion)==1:
        return True

    try:
        int(lista[0])
        try:
            int(lista[1])
            return False
        except ValueError:
            lista.pop(0)
            if len(lista)==1:
                return False
            else:
                return validar_expresion("".join(lista))
    except ValueError:
        try:
            int(lista[1])
            lista.pop(0)
            return validar_expresion("".join(lista))
        except ValueError:
            return False    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           