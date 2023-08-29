def validar_expresion(a):
    a.strip()
    buscar=["+","-","*","/"]

    if len(a)>=3:
        if (a[0]=="-" or a[0] =="+")and a[0] == a[1] :
            return False

    if a.isdigit():
        return True

    else:
        for i in buscar:
           cosa= a.find(i)
           if cosa == -1:
                    continue
           else:
               if i == "+" or i == "-":
                   return validar_expresion(a[cosa+1:])
        else:
            return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           