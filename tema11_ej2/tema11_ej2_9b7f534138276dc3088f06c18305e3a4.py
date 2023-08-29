def validar_expresion(expresion):
    expresion=list(expresion)
    if len(expresion)<3:
        return False
    try:
        a=int(expresion[0])
        b=int(expresion[2])
        a+b
    except:
        return False
    else:
        return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           