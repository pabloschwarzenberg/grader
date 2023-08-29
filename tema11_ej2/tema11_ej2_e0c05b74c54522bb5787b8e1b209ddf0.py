def validar_expresion(expresion):
    lista = []
    str_1 = ""
    for i in expresion:
        if i != "-" and i != "+" and i != " ":
            str_1 += i
        else:
            if str_1 != "":
                lista.append(str_1)
            lista.append(i)
            str_1 = ""
    if str_1 != "":
        lista.append(str_1)
    if len(lista) == 1:
        if lista[0][0].isdigit():
            return True
        else:
            return False
    if len(lista) == 0:
        return False

    for i in range(len(lista)):
        if lista[i][0] in ["+", "-", " "]:
            ex1 = "".join(lista[:i])
            ex2 = "".join(lista[i+1:])
            return validar_expresion(ex1) and validar_expresion(ex2)


if __name__ == "__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
