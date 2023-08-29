def validar_expresion(expresion):
    n1=expresion[0]
    n2=expresion[2]
    sign=expresion[1]
    
    if sign!=("+","-"):
        return False
    else:
        return True

    return validar_expresion(n1+sign+n2)
    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           