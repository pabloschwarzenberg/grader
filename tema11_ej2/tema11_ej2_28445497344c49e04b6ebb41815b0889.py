def validar_expresion(expresion):
    digitos="0123456789"
    if(len(expresion))==0:
        return False
    if expresion.find("+")==-1 and expresion.find("-")==-1:
        return True
    if expresion.find("+")==-1:
        n=expresion.find("-")
    elif expresion.find("-")==-1:
        n=expresion.find("+")
    else:
        n=min(expresion.find("+"),expresion.find("-"))
    if n==0:
        return False
    else:
        Flag=True
        for i in expresion[:n]:
            if i not in digitos:
                Flag=False
        if not Flag:
            return False
        elif n==len(expresion):
            return False
        else:
            return validar_expresion(expresion[n+1:])
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           