def validar_expresion(expresion):
    if len(expresion) == 1:
        try:
            int(expresion)
            return True
        except ValueError:
            return False
    else:
        if len(expresion) % 2 != 0:
            valor = expresion[0]
            try:
                int(valor)
                return validar_expresion(expresion[1:])
            except ValueError:
                return False
        else:
            valor = expresion[0]
            try:
                int(valor)
                return False
            except ValueError:
                return validar_expresion(expresion[1:])


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           