def validar_expresion(expresion):
    digitos = "0123456789"
    signos = "+-"
    if len(expresion) < 3:
        return False
    if expresion[0] in digitos and expresion[2] in digitos and expresion[1] in signos:
        return True
    else:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           