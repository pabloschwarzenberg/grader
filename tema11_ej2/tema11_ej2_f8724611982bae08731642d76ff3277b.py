def validar_expresion(expresion):

    operadores=['+','-']
    numeros=['1','2','3','4','5','6','7','8','9','0']
    a=0
    if expresion[-1] in operadores:
        return False
    for i in expresion:
        if i in numeros:
            a=0
        else:
            a+=1
        if a >1:
            return False
            
    return True
         

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           