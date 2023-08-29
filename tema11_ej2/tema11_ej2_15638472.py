def validar_expresion(expresion):
    n=["1","2","3","4","5","6","7","8","9","0"]
    expresion=str(expresion)
    f=len(expresion)
    p=expresion.find("+")
    s=expresion.find("-")
    if (p==0 or s==0) or expresion[-1]=="-" or expresion[-1]=="+" :
        return False
    else:
        if (expresion[p-1] and expresion[p+1]) not in n:
            return False
        if (expresion[s-1] and expresion[s+1]) not in n:
            return False
        else:
            if len(expresion)==3:
                return True
            expresion=expresion[2:f+1]
            if len(expresion)==0:
                return True
            validar_expresion(expresion)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           