def validar_expresion(expresion):
    if len(expresion) == 1:
        if expresion.isdigit() == True:
            return True
        else:
            return False
    if len(expresion) >= 2:
        if expresion[0].isdigit() == False and expresion[1].isdigit() == False:
            return False
        return validar_expresion(expresion[1:])
        
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))

           