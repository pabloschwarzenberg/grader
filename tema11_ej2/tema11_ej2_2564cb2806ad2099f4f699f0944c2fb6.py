def validar_expresion(expresion):
    if expresion[0].isdigit() and expresion[-1].isdigit():
        return True
    return False


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           