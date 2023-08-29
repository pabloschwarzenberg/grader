def validar_expresion(ex):
    if len(ex)==3:
        if ex[1]=="+" or ex[1]=="-": 
            a=True
        else:
            a=False
        if ex[0]=="1" or ex[0]=="2" or ex[0]=="3" or ex[0]=="4" or ex[0]=="5" or ex[0]=="6" or ex[0]=="7" or ex[0]=="8" or ex[0]=="9": 
            b=True
        else:
            b=False
        if ex[2]=="1" or ex[2]=="2" or ex[2]=="3" or ex[2]=="4" or ex[2]=="5" or ex[2]=="6" or ex[2]=="7" or ex[2]=="8" or ex[2]=="9":
            c=True
        else:
            c=False
        if a==True and b==True and c==True:
            return True
        else:
            return False
    else:
        return False


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           