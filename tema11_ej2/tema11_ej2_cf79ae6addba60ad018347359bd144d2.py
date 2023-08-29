def validar_expresion(expresion,nuevo=""):

    if expresion=="":
        if (nuevo[len(nuevo)-1]=="+") or (nuevo[len(nuevo)-1]=="-"):
            return False
        else:
            return True
    if len(nuevo)==0:
        nuevo=nuevo+expresion[0]
        if nuevo=="+" or nuevo=="-":
            return False
    else:
        if len(expresion)!=0:
            if(expresion[0]=="+" or expresion[0]=="-") and (nuevo[len(nuevo)-1].isdigit()==True): 
                nuevo=nuevo+expresion[0]
            elif(expresion[0].isdigit()==True) and ((nuevo[len(nuevo)-1].isdigit()==True) or (nuevo[len(nuevo)-1]=="+") or (nuevo[len(nuevo)-1]=="-")):
                nuevo=nuevo+ expresion[0]
            else:
                return False

    return validar_expresion(expresion[1:],nuevo)
    
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
    print(validar_expresion("11+2-4++4"))
    print(validar_expresion("1+1+1+1+1+2"))