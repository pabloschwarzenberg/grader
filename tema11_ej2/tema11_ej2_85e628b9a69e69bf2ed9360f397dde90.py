def validar_expresion(exp,d=0):
    if len(exp)==0:
        if d==False:
            return False
        else:
            return True
    d1=exp[0].isdigit()
    if d==d1:
        return False
    else:
        return validar_expresion(exp[1:],d1)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           