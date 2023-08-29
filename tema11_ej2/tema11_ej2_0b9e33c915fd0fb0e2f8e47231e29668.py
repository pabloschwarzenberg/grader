def validar_expresion(expresion):
    a = list(expresion)
    num = "0123456789"
    exp = "+-"
    if len(a) == 1:
        if a[0] in exp:
            return False
        else:
            return True
    else:
        if (a[0] in exp and a[1] in num) or (a[0] in num and a[1] in exp):
            a.pop(0)
            return validar_expresion(a)
        else:
            return False
if __name__=="__main__":
    print(validar_expresion("22+3-5"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           