def validar_expresion(exp):
    numeros = '123456789'
    sr = '+-'
    if len(exp) == 1:
        if exp in numeros:
            return True
        else:
            return False
    else:
        if (exp[0] in numeros and exp[1] in sr) or (exp[0] in sr and exp[1] in numeros):
            return validar_expresion(exp[1:])
        else:
            return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           