def validar_expresion(expresion):
    if expresion.isdigit():
        return True
    if expresion=="-" or expresion=="+":
        return False
    p=expresion.find("+")
    e1=expresion[:p]
    e2=expresion[p+1:]
    print(e1,e2)
    if p!=-1:
        return validar_expresion(e1)and validar_expresion(e2)
    p=expresion.find("-")
    e1=expresion[:p]
    e2=expresion[p+1:]
    print(e1,e2)
    if p!=-1:
        return validar_expresion(e1)and validar_expresion(e2)
    else:
        return False
    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           