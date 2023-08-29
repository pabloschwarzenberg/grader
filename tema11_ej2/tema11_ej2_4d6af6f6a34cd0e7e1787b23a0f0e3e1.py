def validar_expresion(expresion):
    if len(expresion)==1 and expresion[0].isdigit()==False:
        return True
    if expresion[0].isdigit() and expresion[-1].isdigit():
        expresion=expresion.replace(expresion[0],"")
        expresion=expresion.replace(expresion[-1],"")
        validar_expresion(expresion)
        if validar_expresion:
            return True
    else:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           