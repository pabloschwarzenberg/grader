def validar_expresion(expresion):
    if expresion.startswith("x"):
        if expresion[1:] == "1+1":
            return True
    else:
    
        if "-" in expresion:
            expresion = expresion.replace("-","+")
        expresion = list(expresion)
        for i in range(len(expresion)):
            if expresion[i].isnumeric():
                expresion[i] = "1"
        expresion = "".join(expresion)
        if validar_expresion("x"+expresion):
            return True

    return False
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           