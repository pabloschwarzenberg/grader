def validar_expresion(expresion):
    if "+" in expresion == True:
        expresion = expresion.split("+")
        if len(expresion) == 2:
            return True
        else:
            return False
    if "-" in expresion == True:
        expresion = expresion.split("-")
        if len(expresion) == 2:
            return True
        else:
            return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           