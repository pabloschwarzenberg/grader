def validar_expresion(expresion):
    if len(expresion)==3:
        if expresion[0].isdigit():
            return validar_expresion(expresion[1:])
        else:
            return False
    if len(expresion)==2:
        if expresion[0] is "+":
            return validar_expresion(expresion[1:])
        elif expresion[0] is "-":
            return validar_expresion(expresion[1:])
        else:
            return False
    if len(expresion)==1:
        if expresion[0].isdigit():
            return True
        else:
            return False
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           