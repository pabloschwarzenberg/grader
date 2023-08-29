def validar_expresion(expresion):
    num=[1,2,3,4,5,6,7,8,9,0]
    expresion=list(expresion)

    if len(expresion)==1:
        if  expresion[0]=="+" or expresion[0]=="-":
            return False
        else:
            return True

    for i in range (len(num)):
        if expresion[0]== str(num[i]):
            expresion.remove(expresion[0])
            return validar_expresion("".join(expresion))


    if expresion[0]=="+" or expresion[0]=="-":
        for i in (num):
            if expresion[1] == str(num[i]):
                expresion.remove(expresion[0])
                return validar_expresion("".join(expresion))
        return False


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           