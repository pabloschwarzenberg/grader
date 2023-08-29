def validar_expresion(expresion):
    expresion = list(expresion)
    a=len(expresion)
    if expresion[a-1] == '-' or expresion[a-1] == '+':
        return False
    elif expresion[0] == '+' or expresion[0] == '-':
        if expresion[1] == '+' or expresion[1] == '-':
            return False
        else:
            return validar_expresion(expresion[1:])
    elif len(expresion) == 1:
            return True
    elif expresion[0] != '+' and expresion[0] != '-':
        return validar_expresion(expresion[1:a])
      

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           