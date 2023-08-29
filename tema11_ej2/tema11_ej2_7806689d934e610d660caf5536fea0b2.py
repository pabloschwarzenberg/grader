def validar_expresion(expresion,nuevo=""):
    if len(nuevo)==0:
         nuevo=expresion[0]
         if nuevo=="+" or nuevo=="-":
             return False
    else:
        if len(expresion)!=0:
            if (expresion[0]=="+" or expresion[0]=="-") and nuevo[len(nuevo)-1].isdigit()==True:
                nuevo=nuevo+expresion[0]
            elif expresion[0].isdigit()==True and (nuevo[len(nuevo)-1].isdigit()==True or nuevo[len(nuevo)-1]=="+" or nuevo[len(nuevo)-1]=="-"):
                nuevo=nuevo+expresion[0]
            else:
                return False
            
    if len(expresion)==0:
        if nuevo[len(nuevo)-1]=="+" or nuevo[len(nuevo)-1]=="-":
            return False
        else:
            return True
        
    return validar_expresion(expresion[1:],nuevo)
   

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))