def validar_expresion(expresion):

    if expresion[0] == "+" or expresion[0] == "-":
        return False

    elif expresion[len(expresion)-1] == "+" or expresion[len(expresion)-1] == "-":
        return False

    q = len(expresion) - 1
    if q == 0:
        return True
    
    else:
        if expresion[q] == "+" or expresion[q] == "-":
            if expresion[q - 1] == "+" or expresion[q - 1] == "-":
                return False
            
        else:
            return validar_expresion(expresion[0:q-1])    
    
    
        

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           