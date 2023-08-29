def validar_expresion(expresion):
    l = []
    for k in expresion:
        l.append(k)
    if (l[0] != "+" and l[0] != "-") and (l[len(l)-1] != "+" and l[len(l)-1] != "-"):
        for i in l:
            if not(l.index(i) != 0 and l.index(i) < len(l) and ((i == "+" or i == "-") and (l[l.index(i)- 1] != i and l[l.index(i)+ 1] != i))):
                return False
        return True
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           