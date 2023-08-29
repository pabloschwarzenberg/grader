def validar_expresion(expresion):
    if len(expresion) == 0:
        return True
    elif len(expresion) == 1:
        if expresion.isdigit() == True:
            return True
        else:
            return False
    elif len(expresion) > 2:
        if expresion[0].isalpha() == False and expresion[0].isdigit() == False:
            if expresion[1].isdigit() == True:
                expresion = expresion[2:]
                return validar_expresion(expresion)
            else:
                return False
        elif expresion[0].isdigit() == True:
            if expresion[1].isalpha() == False and expresion[1].isdigit() == False:
                if expresion[2].isdigit() == True:
                    expresion = expresion[3:]
                    return validar_expresion(expresion)
                else:
                    return False
            else:
                return False
    elif len(expresion) == 2:
        if expresion[0].isalpha() == False and expresion[0].isdigit() == False:
            if expresion[1].isdigit()== True:
                return True
            else:
                return False
        else:
            return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           