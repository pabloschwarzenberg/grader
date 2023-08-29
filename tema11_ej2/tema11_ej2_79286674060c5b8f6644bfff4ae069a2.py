def validar_expresion(expresion,simbolo=0):
    if len(expresion)>1 :
        if (expresion[0].isnumeric() and expresion[-1].isnumeric()) or (expresion[0] in ["+","-","/","*"] and expresion[-1] in ["+","-","/","*"]):
            return validar_expresion(expresion[1:-1],simbolo+1)
        else:
            return False

    else:
        if simbolo%2:
            if expresion in ["+","-","/","*"]:
                return True
            else:
                return False
        else:
            if expresion.isnumeric():
                return True
            else:
                return False


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           