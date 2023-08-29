def validar_expresion(expresion):
    if "-" in expresion:
        k="-"
        l=expresion.split("-")
    elif "+" in expresion:
        k="+"
        l=expresion.split("+")
    a=l[0]
    b=l[1]
    if a=="" or b=="":
        return False
    if len(l)>2:
        return False
    def operacion(a,b,k):
        if "+" or "-" in a:
            return False
        if "+" or "-" in b:
            return False
        else:
            a=int(a)
            b=int(b)
            if k=="+":
                return a+b
            elif k=="-":
                return a-b
    if isinstance(operacion(a,b,k),int):
        return True
    else:
        return False
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))

