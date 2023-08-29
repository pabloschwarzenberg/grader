def validar_expresion(expresion):
    expresion=list(expresion)
    if len(expresion)<3:
        return False
    for i in range(len(expresion)):
        if expresion[0]=="+" or expresion[0]=="-":
            return False
        elif expresion[2]=="+" or expresion[2]=="-":
            return False
    return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))

