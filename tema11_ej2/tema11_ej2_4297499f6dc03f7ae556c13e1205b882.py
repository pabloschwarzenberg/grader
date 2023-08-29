def validar_expresion(expresion):
    signos = ["+", "-"]
    if len(expresion) == 2:
        if expresion[1] not in signos:
            return True
        else:
            return False
    if len(expresion) not in (0, 1):
        if expresion[0] not in signos:
            return validar_expresion(expresion[2:])
    if len(expresion) == 1:
        if expresion not in signos:
            return True
    if len(expresion) == 0:
        return True
    else:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))

           