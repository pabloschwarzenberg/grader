def validar_expresion(expresion):
    if len(expresion)<4:
        if len(expresion)==3:
            if expresion[0].isdigit() and expresion[2].isdigit():
                if expresion[1]=="+" or expresion[1]=="-":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        if expresion[0].isdigit() and expresion[2].isdigit():
            if expresion[1]=="+" or expresion[1]=="-":
                expresion=expresion.strip(expresion[0])
                expresion = expresion.strip(expresion[0])
                expresion = expresion.strip(expresion[0])
                return validar_expresion(expresion)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           