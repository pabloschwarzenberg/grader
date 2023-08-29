def validar_expresion(expresion):
    operaciones=["-","+","*","/"]
    if len(expresion)<3:
        return False
    if expresion[0].isdigit()==False:
        return False
    elif expresion[1].isdigit()==False and expresion[2].isdigit()==False:
        return False
    else:
        return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           