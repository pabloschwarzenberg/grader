def validar_expresion(expresion):
    if expresion[0] == "+" or expresion[-1] == "+" or expresion[0] == "-" or expresion[-1] == "-":
        return False
    else:
        return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           