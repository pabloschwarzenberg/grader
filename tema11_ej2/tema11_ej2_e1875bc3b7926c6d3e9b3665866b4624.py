def validar_expresion(expresion):
    l_expresion = list(expresion)
    if len(l_expresion) > 2:
        if l_expresion[0] == "-" or l_expresion[0] == "+":
            if l_expresion[-1] == "-" or l_expresion[-1] == "+":
                l_expresion = l_expresion[1:-1]
                c_l_expresion = l_expresion
                validar_expresion("".join(c_l_expresion))

    if len(l_expresion) > 2:
        if l_expresion[0] in ["1","2","3","4","5","6","7","8","9"]:
            if l_expresion[-1] in ["1","2","3","4","5","6","7","8","9"]:
                l_expresion = l_expresion[1:-1]
                c_l_expresion = l_expresion

                validar_expresion("".join(c_l_expresion))

    if len(l_expresion) == 1 or len(l_expresion) == 0:
        return True
    else:
        return False