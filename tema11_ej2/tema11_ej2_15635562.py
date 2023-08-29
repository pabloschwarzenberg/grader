def validar_expresion(expresion):
    if len(expresion)==1 and (expresion=="+" or expresion=="-"):
        return True
    if (expresion[0]=="+" or expresion[0]=="-") or (expresion[len(expresion)-1]=="+" or expresion[len(expresion)-1]=="-"): 
        return False
    else:
        e=expresion[1:len(expresion)-1]
        return validar_expresion(e)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))

           