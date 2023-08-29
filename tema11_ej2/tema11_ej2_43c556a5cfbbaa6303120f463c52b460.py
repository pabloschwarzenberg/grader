def validar_expresion(expresion):
    a= list(expresion)
    if len(a) == 2:
        if a.count("+") == 2 or a.count("-") == 2:
            return False
        elif a[1] == "+" or a[1] == "-":
            return False
        elif a[0] != "+" and a[0] != "-":
            return True
        else:
            return True

    elif len(a) != 2:
        a = list(expresion)
        cabeza = a.pop(0)
        expresion = "".join(a)
        if validar_expresion(expresion) == True:
            a = list(expresion)
            if cabeza != "-" and cabeza != "+":
                return True
            elif (cabeza == "+" or cabeza == "-") and (a[0] != "+" and a[0] != "-"):
                return True

            else:
                return False

        elif validar_expresion(expresion) == False:
            return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           