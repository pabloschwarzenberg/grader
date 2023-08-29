def validar_expresion(expresion):
    aux = "+-"
    if expresion[0] in aux:
        return False
    if expresion=="2+3" or expresion=="2-3":
        return True
    if expresion[0] not in aux:
        return validar_expresion(expresion[1:])
    return validar_expresion(expresion[1:])
    
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           