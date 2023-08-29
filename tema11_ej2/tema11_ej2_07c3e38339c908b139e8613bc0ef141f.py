def validar_expresion(expresion):
    signos = "+-"
    if len(expresion) == 2:
        if expresion[1] not in signos:
            return True
        else:
            return False

    if expresion[0] in signos:
        if expresion[1] not in signos:
            return(validar_expresion(expresion[1:]))
        else:
            return False

    if expresion[0] not in signos:
        return(validar_expresion(expresion[1:]))