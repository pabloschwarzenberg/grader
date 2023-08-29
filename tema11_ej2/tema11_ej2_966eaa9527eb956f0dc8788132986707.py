def validar_expresion(n):
    if n.isdigit():
        return n.isdigit()
    elif n == ('+' or '-'):
        return False
    else:
        for i in ['+','-']:
            p = n.find(i)
            if p != -1:
                return bool(validar_expresion(n[:p]) and validar_expresion(n[p+1:]))
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))