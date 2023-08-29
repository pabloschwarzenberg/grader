def validar_expresion(e):

    verdad=0
    if e[0].isalnum()== False:
        verdad+=1
    if e[-1].isalnum()== False:
        verdad+=1
    for i in range (1,len(e)-1):
        if e[i].isalnum()== False and e[i+1].isalnum()== False :
            verdad+=1 

        
    if verdad==0:
        return True
    elif verdad!=0:
        return False 

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           