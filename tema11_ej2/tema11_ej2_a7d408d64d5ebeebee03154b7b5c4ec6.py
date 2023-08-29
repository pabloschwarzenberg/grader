lista=["1","2","3","4","5","6","7","8","9"]
def validar_expresion(expresion):
    if len(expresion)==3:
        if expresion[0] not in lista or expresion[2] not in lista or expresion[1] in lista:
            return False
        else:
            return True
    else:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           