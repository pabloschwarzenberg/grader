def validar_expresion(exprecion):
    if "+" not in exprecion and "-" not in exprecion:
        numeros = "0123456789"
        if "" == exprecion:
            return False
        else:
            for letra in exprecion:
                if letra not in numeros:
                    return False
        return True
    else:
        encontrado = False
        i = 0
        while not encontrado:
            if (exprecion[i] == "+") or (exprecion[i] == "-"):
                validez1 = validar_expresion(exprecion[:i])
                validez2 = validar_expresion(exprecion[i + 1:])
                return validez1 and validez2
            i += 1


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
