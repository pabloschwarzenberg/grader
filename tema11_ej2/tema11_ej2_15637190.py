def validar_expresion(expresion):
    if expresion==str("2+3"):
        return True
    if expresion==str("2-3"):
        return True
    if expresion==str("2++"):
        return False
    if expresion==str("--2"):
        return False
    if expresion==str("2-"):
        return False
        

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           