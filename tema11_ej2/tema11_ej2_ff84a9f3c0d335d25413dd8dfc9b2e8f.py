def validar_expresion(expresion):
    operadores=["+","-"]
    for i in operadores:
        m=expresion.find(i)
        if m!= -1:
            izq=expresion[0:m]
            der=expresion[m+1:]
            if izq=="" or der=="" or izq=="+" or der=="+" or izq=="-" or der=="-":
                return False
            else:
                return validar_expresion(der)
    return True
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           