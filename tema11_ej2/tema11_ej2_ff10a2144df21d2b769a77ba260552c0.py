def validar_expresion(expresion):
    try:
        a=eval(expresion)
        int(expresion[0])
        int(expresion[2])
        return True
    except:
        return False
    
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
