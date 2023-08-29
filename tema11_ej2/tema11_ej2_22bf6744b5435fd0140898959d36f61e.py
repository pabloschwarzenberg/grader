def validar_expresion(expresion):

    expresion=list(expresion)

    if len(expresion)==1:
        return True

    elif len(expresion)%2==0:
        return False
    
    else:
        if expresion[0].isdigit()==expresion[-1].isdigit():
            expresion.pop(-1)
            expresion.pop(0)
            return validar_expresion(expresion)

        else:
            return False
            

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           