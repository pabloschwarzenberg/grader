def validar_expresion(expresion):
    if expresion.isnumeric():
        return True
    for i in range(0,len(expresion)):
        if expresion[0].isnumeric():
            if expresion[i] == "+":
                try:
                    if expresion[i+1] in ("+","-"):
                        return False
                    else:
                        b=list(expresion)
                        b.pop(i)
                        return validar_expresion("".join(b))
                except: IndexError
                return False
            if expresion[i] == "-":
                try:
                    if expresion[i+1] in ("+","-"):
                        return False
                    else:
                        b=list(expresion)
                        b.pop(i)
                        return validar_expresion("".join(b))
                except: IndexError
                return False
        elif expresion[0]=="-" and expresion[1].isnumeric():
            b = list(expresion)
            b.pop(0)
            return validar_expresion("".join(b))
        else:
            return False
            


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           