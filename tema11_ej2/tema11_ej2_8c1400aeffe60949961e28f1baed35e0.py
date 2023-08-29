def validar_expresion(expresion):
    p="+-*/"
    for i in range(0,len(p)):
        if expresion[0]==p[i] or expresion[-1]==p[i]:
            return False
    return True
    
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           