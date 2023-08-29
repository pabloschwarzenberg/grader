
def validar_expresion(expresion):

        if expresion[-1] == "+" or expresion[-1] == "-" or expresion[0] == "+" or expresion[0] == "-":
            return False

        if expresion[0].isnumeric() == True:
            return True
        else:
            expresion == expresion[1:]
            