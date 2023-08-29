def validar(expresion,n):
    operators=["-","+","%","*","**"]
    if n==len(expresion):
        if expresion[n-1].isdigit():
            return True
        else:
            return False
    elif n%2==0:
        if expresion[n].isdigit():
            return validar(expresion,n+1)
        else:
            return False
    elif n%2!=0:
        if expresion[n] in operators:
            return validar(expresion,n+1)
        else:
            return False
        
    
def validar_expresion(expresion):
    espresion=list(expresion)
    return validar(expresion,0)
    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
