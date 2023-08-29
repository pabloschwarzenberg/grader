def validar_expresion(expresion):
    if len(expresion)==1:
        if expresion=="+" or expresion=="-" or expresion=="*" or expresion=="/":
            return True
        else:
            return False
    else:
        if expresion[0].isdigit() and expresion[-1].isdigit():
            e0=expresion.lstrip(expresion[0])
            e1=e0.rstrip(expresion[-1])
            expresion_nueva=validar_expresion(e1)
            return expresion_nueva
        else:
            return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           