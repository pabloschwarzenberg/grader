def validar_expresion(expresion):
    if len(expresion) == 0:
        return True
    elif expresion[0].isdigit() == False:
        return False
    elif len(expresion) != 2:
        return validar_expresion(expresion[2::2])
    elif len(expresion) == 2:
        return False
    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           