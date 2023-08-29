def validar_expresion(expresion):
    if len(expresion) == 1:
        try:
            a = int(expresion)
            return True
        except:
            return False
    while True:
        if validar_expresion(expresion[0]):
            if len(expresion) == 1:
                return True
            elif expresion[1] == "+" or expresion[1] == "-":
                try:
                    expresion = expresion[2:]
                    return validar_expresion(expresion)
                except:
                    return False
            else:
                expresion = expresion[1:]
        else:
            return False
 
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           