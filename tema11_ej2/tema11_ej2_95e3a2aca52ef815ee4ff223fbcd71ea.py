def validar_expresion(expresion):
    if expresion == "0":
        return True
    else:
        expresion = int(expresion)
        if expresion = expresio.is_integer()
            return True
        else:
            return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           