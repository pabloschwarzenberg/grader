def validar_expresion(expresion):
    mas = expresion.count("+")
    menos = expresion.count("-")
    print(mas)
    print(menos)
    if mas > 1 or menos > 1:
     return False
    elif (mas == 1 or menos == 1) and len(expresion) == 3 :
     return True
    else :
     return False
    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           