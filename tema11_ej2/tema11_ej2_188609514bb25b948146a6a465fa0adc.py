def validar_expresion(expresion):
    if expresion.isnumeric():
        return True
    else:
        if expresion[0].isnumeric():
            expresion = expresion[1:]
            return validar_expresion(expresion)
        else:
            expresion = expresion[1:]
            if expresion == "":
                return False
            elif expresion[0].isnumeric():
                return validar_expresion(expresion)
            else:
                return False




if __name__ == "__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           