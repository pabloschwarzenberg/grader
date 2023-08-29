def validar_expresion(expresion):
    numeros=["1","2","3","4","5","6","7","8","9","0"]
    if expresion=="+" or expresion=="-":
        return True
    if len(expresion)==3:
        if expresion[0] in numeros and expresion[2] in numeros:
            return validar_expresion(expresion[1])
    if len(expresion)!=3:
        return False
    else:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           