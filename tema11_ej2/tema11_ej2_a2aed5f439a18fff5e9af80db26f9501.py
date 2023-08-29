def validar_expresion(expresion):
    carac ="+-"
    if len(expresion) >= 3:
        for i in range(len(expresion)):
            if (expresion[i] == "+" or expresion[i] == "-") and (expresion[i-1] not in carac and expresion[i+1] not in carac):
                print(expresion[i+1] not in carac)
                return True
        else:
            return False
    else:
        return False
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           