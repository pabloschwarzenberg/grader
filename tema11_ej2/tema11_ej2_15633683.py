def validar_expresion(expresion):
    if len(expresion)==0:
        return True
    if expresion[0]=="+" or expresion[0]=="-" or expresion[len(expresion)-1]=="+" or expresion[len(expresion)-1]=="-":
        return False
    else:
        return validar_expresion(expresion[2:(len(expresion)-2)])
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           