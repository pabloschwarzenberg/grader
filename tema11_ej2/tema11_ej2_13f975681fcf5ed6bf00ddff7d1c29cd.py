def validar_expresion(expresion):
    if expresion[0]=="+" or expresion[0]=="-":
        return False
    if expresion[-1]=="-" or expresion[-1]=="+":
        return False
    if expresion[0].isnumeric()==True:
        return True
    else:
       expresion=expresion[1:]
       return validar_expresion(expresion)
    

    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
