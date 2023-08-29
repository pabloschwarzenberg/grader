def validar_expresion(expresion):
    if len(expresion)<2:
        try:
            expresion=int(expresion)
            return True
        except ValueError:
            return False
    operadores=["+","-","/","*"]
    if expresion[0] in operadores and expresion[1] not in operadores:
        return True and validar_expresion(expresion[1:])
    try:
        numero=int(expresion[0])
        return True and validar_expresion(expresion[1:])
    except ValueError:
        return False and validar_expresion(expresion[1:])
        


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))