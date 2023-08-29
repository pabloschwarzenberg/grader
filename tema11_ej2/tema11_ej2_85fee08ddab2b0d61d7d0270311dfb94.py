def validar_expresion(expresion):
    numeros="0123456789"
    if len(expresion)==0:
        if expresion in numeros:
            return True
        else:
            return False
    else:
        for i in expresion:
            resultado = validar_expresion(i)
    return resultado
            
    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           