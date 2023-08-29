def validar_expresion(expresion):
    if len(expresion) == 2:
        a = expresion[0]
        b = expresion[1]
        if a in '+-1234567890':
            if b in '+-':
                return False
            elif b in '1234567890':
                return True
        else:
            return False
    else:
        return validar_expresion(expresion[:len(expresion)-2])

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           