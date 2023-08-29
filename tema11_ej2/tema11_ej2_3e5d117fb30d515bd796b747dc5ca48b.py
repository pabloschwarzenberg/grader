def validar_expresion(expresion):
    # asumiendo que solo entregan operaciones binomiales
    if len(expresion) ==  0:
        return True

    if len(expresion) in [1,3]:
        try:
            int(expresion[0])
        except ValueError:
            return False
        else:
            return validar_expresion(expresion[1:])
    else:
        if expresion[0] in ['+','-']:
            return validar_expresion(expresion[1:])
        else:
            return False


if __name__ == "__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
