def validar_expresion(expresion,indice=0):
    string=list(expresion)
    if expresion[0]=="+" or expresion[0]=="-" or expresion[len(expresion)-1]=="+" or expresion[len(expresion)-1]=="-":
        return False
    else:
        if indice==len(expresion)-1:
            return True
        if (expresion[indice]=="+" or expresion[indice]=="-") and (expresion[indice+1]=="+" or expresion[indice+1]=="-"):
            return False
        indice+=1
        return validar_expresion(expresion,indice)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           