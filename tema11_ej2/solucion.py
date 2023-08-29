def validar_expresion(s):
    suma=s.find("+")
    resta=s.find("-")
    if suma==-1 and resta==-1:
        if s.isdigit():
            return True
        else:
            return False
    elif suma!=-1 and resta!=-1:
        operador=min(suma,resta)
    elif suma!=-1:
        operador=suma
    elif resta!=-1:
        operador=resta
    a=s[:operador]
    if not a.isdigit():
        return False
    b=s[operador+1:]
    return validar_expresion(b)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
    print(validar_expresion("2+3-11"))
    print(validar_expresion("2-3+8"))
