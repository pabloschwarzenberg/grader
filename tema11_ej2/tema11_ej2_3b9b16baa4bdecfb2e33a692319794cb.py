def validar_expresion(expresion):
    if "+" not in expresion and "-" not in expresion and "*" not in expresion:
        numeros = "0123456789"
        if "" == expresion:
            return False
        else:
            for letra in expresion:
                if letra not in numeros:
                    return False
                return True
    else:
        encontrado = False
        i=0
        while not encontrado:
            if expresion[i] == "+" or expresion[i] == "-" or expresion[i]=="*":
                encontrado = True
                validez1 = validar_expresion(expresion[:i])
                validez2 = validar_expresion(expresion[i+1:])
                return validez1 and validez2
            i+=1
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           