def validar_expresion(expresion):
    if '-' not in expresion and '+' not in expresion:
        return False
    ultimo_simbolo = -2
    j = 0
    for i in expresion:
        if i in '0123456789()+-':
            if i in '()+-':
                if ultimo_simbolo == j - 1:
                    return False
                else:
                    ultimo_simbolo = j
            if i in '(+-' and len(expresion) == j + 1:
                return False
        else:
            return False
        j += 1
    return True
