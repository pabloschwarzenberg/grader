def validar_expresion(exp):
    if exp.isdigit():
        return True
    if not exp[0].isdigit():
        return False
    if not exp[-1].isdigit():
        return False
    pos = 0
    for i in range(len(exp)):
        if not exp[i].isdigit():
            pos = i
            break
    return validar_expresion(exp[:pos]) and validar_expresion(exp[pos+1:])

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           