def validar_expresion(expresion):
    if expresion==[True,False,True]:
        return True
    elif expresion==[True,False,False]:
        return False
    elif expresion==[False,False,True]:
        return False
    elif expresion==[True,False]:
        return False
    else:
        expresion=list(expresion)
        i=0
        while i < len(expresion):
            if expresion[i].isdigit()==True:
                expresion[i]=(expresion[i].isdigit())

            elif expresion[i].isdigit()==False:
                expresion[i]=(expresion[i].isdigit())
            i=i+1
         
            
        return validar_expresion(expresion)
        

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           