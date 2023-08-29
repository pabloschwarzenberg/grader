def validar_expresion(expresion):
    if len(expresion) == 1:
        return True
    if expresion[0].isnumeric() and expresion[-1].isnumeric():
        expresion = expresion[1:-1]
        return validar_expresion(expresion)
    if expresion[0].isnumeric() == False and expresion[-1].isnumeric() == False:
        expresion = expresion[1:-1]
        return validar_expresion(expresion)
    else:
        return False
    
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           