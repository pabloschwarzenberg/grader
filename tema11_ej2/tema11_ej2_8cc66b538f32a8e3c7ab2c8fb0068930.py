def validar_expresion(expresion):
    if expresion[len(expresion)-1]=="-" or expresion[len(expresion)-1]=="+":
        x=False
    elif len(expresion)==1:
        x=True
    elif expresion[0]=="-" or expresion[0]=="+":
        if expresion[1]!="-" and expresion[1]!="+":
            x=validar_expresion(expresion[1:])
        else:
            x=False
    elif expresion[0]!="-" and expresion[0]!="+":
        if expresion[1]=="-" or expresion[1]=="+":
            x=validar_expresion(expresion[1:])
        else:
            x=False
    return x
    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           
