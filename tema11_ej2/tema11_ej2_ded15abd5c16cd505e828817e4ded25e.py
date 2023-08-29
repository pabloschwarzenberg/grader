def validar_expresion(expresion):
    if not expresion[0].isdigit():
        return False
    else:
        for n in range(len(expresion)):
            if expresion[n].isdigit():
                numero=1
            if expresion[n]=="+" or expresion[n]=="-":
                signo=1
                if n==len(expresion)-1:
                    return False
                if not (expresion[n-1].isdigit() and expresion[n+1].isdigit()):
                    return False
        if numero==1 and signo==1:
            return True
    return

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           