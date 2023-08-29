def validar_expresion(expresion):
    contador = 0
    for n in expresion:
        if n == "-" or n == "+":
            try:
                siguiente = expresion[contador + 1]
                if siguiente == "-" or siguiente == "+":
                    return False
            except IndexError:
                return False
        contador += 1
    return True

if __name__ == "__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
