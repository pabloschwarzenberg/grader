def validar_expresion(expresion):
    if len(expresion) == 0:
        return False
    if expresion[0] == "+" or expresion[0] == "-":
        return False
    if len(expresion) == 1:
        return True
    else:
        return validar_expresion(expresion[2:])

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           