def validar_expresion(expresion):
    if '+' in expresion:
        expresion=expresion.split('+')
    elif '-' in expresion:
        expresion=expresion.split('-')
    for i in expresion:
        try:
            i=int(i)
        except:
            return False
    return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           