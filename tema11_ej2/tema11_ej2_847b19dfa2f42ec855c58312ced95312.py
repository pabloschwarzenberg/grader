def validar_expresion(expresion):
    if expresion[0].isnumeric== True:
        lista =["+","-"]
        if expresion[1] in lista:
            if expresion[2].isnumeric== True:
                return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           