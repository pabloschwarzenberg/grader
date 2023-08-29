def validar_expresion(expresion):
    if len(expresion)==0:
        return False
    if not expresion[0].isdigit():
        return False
    if "-" not in expresion and "+" not in expresion:
        return True
    a,b=expresion.find("+"),expresion.find("-")
    if (a>b and b>=0) or a<0:
        a=b
    return validar_expresion(expresion[a+1:])

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           