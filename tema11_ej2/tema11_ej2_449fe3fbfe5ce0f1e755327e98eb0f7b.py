def validar_expresion(expresion,i=0):
    if expresion=='':
        return True
    elif expresion[0].isdigit():
        i += 1
        return validar_expresion(expresion[1:],i)
    elif expresion[0]=='+' or expresion[0]=='-':
        if len(expresion)==1 or i==0:
            return False
        if not expresion[1].isdigit():
            return False
        i += 1
        return validar_expresion(expresion[1:],i)
    else:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           