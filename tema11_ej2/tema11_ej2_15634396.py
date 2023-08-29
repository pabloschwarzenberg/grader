def validar_expresion(expresion):
    a=list(expresion)
    lista1=['+','-',]
    if a[-1] in lista1:
        return False
    elif a[0] in lista1 and a[1] in lista1:
        return False
    else:
        a=a.pop(0)
        jojojo=''.join(a)
        if len(jojojo)==1:
            return True
        else:
            validar_expresion(jojojo)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           