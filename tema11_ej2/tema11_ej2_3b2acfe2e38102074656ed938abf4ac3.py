def validar_expresion(expresion):
    e=list(expresion)
    print(e)
    for i in range(0,len(e)):
        if (e[i]=="+" and e[i+1]=="+") or (e[i]=="-" and e[i+1]=="-"):
            return False
        elif (e[i]=="+") or (e[i]=="-"):
            return True
        if len(e)<3:
            return False

    
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))