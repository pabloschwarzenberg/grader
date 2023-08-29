def validar_expresion(expresion):
    operaciones=["+","-","*","/"]
    for op in operaciones:
        if op in expresion:
            for n in range(0,len(expresion)):
                if expresion[n]==op:
                    if n!=len(expresion)-1:
                        if expresion[n+1].isnumeric():
                            pass
                        else:
                            return False
                    else:
                        return False
    return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           