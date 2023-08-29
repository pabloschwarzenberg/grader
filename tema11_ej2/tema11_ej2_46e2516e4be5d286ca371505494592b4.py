def validar_expresion(expresion):
    if expresion[0]=="+" or expresion[0]=="-" or expresion[len(expresion)-1]=="+" or expresion[len(expresion)-1]=="-":
        return False
    else:
        if expresion[1]=="+" or expresion[1]=="-":
            if expresion[0]=="2" or expresion[0]=="3" and expresion[1]=="2" or expresion[1]=="3":
                return True
        else:
            return False




if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           