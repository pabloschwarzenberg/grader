A = None
def validar_expresion(expresion):
    global A
    expresion = list(expresion)
    if len(expresion) > 0:
        if expresion[0].isdigit():
            expresion.remove(expresion[0])
            "".join(expresion)
            validar_expresion(expresion)
        elif expresion[0] == "+" or expresion[0] == "-":
            if len(expresion) > 1:
                if expresion[1] == "+" or expresion[1] == "-":
                    A = False
                else:
                    expresion.remove(expresion[0])
                    "".join(expresion)
                    validar_expresion(expresion)
                    A = True
            else:
                A = False
    return A

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           