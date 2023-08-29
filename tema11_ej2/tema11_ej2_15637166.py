def validar_expresion(expresion):
    a=expresion
    conteo=0
    conteo1=0
    for i in a:
        if i=="+":
            conteo+=1
            if i==a[-1]:
                conteo+=1            
    for i in a:
        if i=="-":
            conteo1+=1
            if i==a[-1]:
                return False 
    if conteo>1:
        return False
        
    elif conteo1>1:
        return False
    
    else:
        return True

    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           