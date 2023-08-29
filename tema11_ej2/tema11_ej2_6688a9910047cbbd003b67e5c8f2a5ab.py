def validar_expresion(expresion,elemento = "entero"):
    if len(expresion) == 1 and expresion != "+" and expresion != "-":
        return True
    elif len(expresion) == 1:
        return False
    
    elif elemento == "entero":
        if expresion[0] != "+" and expresion[0] != "-":
            expresion2 = expresion[1:]
            return validar_expresion(expresion2,"operador")
        else:
            return False
    else:
        if expresion[0] == "+" or expresion[0] == "-":
            expresion2 = expresion[1:] 
            return validar_expresion(expresion2)
        else:
            return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           