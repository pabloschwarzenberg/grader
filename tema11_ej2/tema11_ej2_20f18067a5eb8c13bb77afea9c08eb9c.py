def validar_expresion(expresion):
    if len(expresion)==3 and expresion[0].isdigit()==False:
        return False
    elif len(expresion)==2 and expresion[0].isdigit()==True:
        return False
    elif len(expresion)==1 and expresion[0].isdigit()==False:
        return False
    elif len(expresion)==1 and expresion[0].isdigit()==True:
        return True
    else:
        l=list(expresion)
        del(l[0])
        n_expresion=''.join(l)
        return validar_expresion(n_expresion)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           