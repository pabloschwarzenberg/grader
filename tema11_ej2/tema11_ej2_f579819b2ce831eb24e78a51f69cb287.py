def validar_expresion(expresion):
    if len(expresion) == 1 and expresion.isnumeric() == False:
        return True
    else:
        a = expresion[0]
        b = expresion[-1]
        if a.isnumeric() == True and b.isnumeric() == True:
            c = expresion[1:-1]
            if len(c) == 1:
                return validar_expresion(c)
            else:
                d = c[0]
                e = c[-1]
                if d.isnumeric() == False and e.isnumeric == False:
                    f = c[1:-1]
                    return validar_expresion(f)
                else:
                    return False
        else:
            return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           