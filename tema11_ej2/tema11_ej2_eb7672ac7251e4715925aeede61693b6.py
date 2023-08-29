def validar_expresion(expresion):
    digitos="0123456789"
    if len(expresion)==2:
        if expresion[0] in digitos and expresion[1] in digitos:
            return True
        else:
            return False
    else:
        l = list(expresion)
        for i in l:
            if i not in digitos:
                l.remove(i)
                break
        a="".join(l)
        return validar_expresion(a)



if __name__ == "__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
