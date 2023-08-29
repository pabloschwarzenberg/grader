def validar_expresion(expresion):
    num = "1234567890"
    op = "+-"
    if expresion[len(expresion)-1] not in num:
        return False
    elif expresion[0] in op and expresion[1] in op:
        return False
    if len(expresion)<=3:
        return True
    else:
        return validar_expresion(expresion[1:])

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           