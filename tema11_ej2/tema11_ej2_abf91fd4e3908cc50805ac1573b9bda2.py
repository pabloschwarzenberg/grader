def validar_expresion(expresion):

    if expresion[0].isdigit() is True:
        if len(expresion) > 1:
            return validar_expresion(expresion[1:])
        if len(expresion) == 1:
            return True
    if expresion[0]=="-" or expresion[0]=="+":
        if len(expresion) >= 2:
            if expresion[1].isdigit() is True:
                return validar_expresion(expresion[1:])
        else:
            return False
    if expresion[0].isdigit() is False or expresion[0 ] !="+" or expresion[0 ] !="-":
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           