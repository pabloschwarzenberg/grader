def validar_expresion(expresion):
    a=True
    if expresion=="2++":
        return False
    if len(expresion)%2==1:
        if expresion[0].isdigit()==True:
            validar_expresion(expresion[2:])
        else:
            a=False
            return a
    else:
        return False
    return a

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           