def validar_expresion(expresion):
    expresion=list(expresion)
    print(expresion)
    if len(expresion)==2:
        if expresion[0]!="+" and expresion[0]!="-":
            if expresion[0]=="+" or expresion[1]=="-":
                return False
        
    if len(expresion)==3:
        if expresion.count("+")==1 and expresion.count("-")==1:
            return False
        if expresion.count("+")==2 or expresion.count("-")==2:
            return False
        if expresion[0]!="+" or expresion[0]!="-":
            if expresion[1]=="-" or expresion[1]=="+":
                if expresion[0]!="+" or expresion[0]!="-":
                    return True
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           