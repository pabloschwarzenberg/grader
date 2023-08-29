def validar_expresion(expresion):
    if expresion.isdigit():
        return float(expresion)
    operadores=["+","-"]
    
    for i in operadores:
        p=expresion.find(i)
        if p!=-1:
            a=expresion[:p]
            b=expresion[p+1:]
            if a.isdigit()==True and b.isdigit()==True:
                return True
            else:
                return False         
        
        
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           