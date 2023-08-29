def validar_expresion(expresion):
    if len(expresion) == 0:
        return False
    if len(expresion) == 1:
        if expresion.isdigit():
            return True
        return False
    else:
        if expresion.count("+") > 0 and expresion.count("-") == 0:
          posicion = expresion.index("+")
          return validar_expresion(expresion[:posicion]) and validar_expresion(expresion[posicion +1 :])
        if expresion.count("+") == 0 and expresion.count("-") > 0: 
          posicion = expresion.index("-")
          return validar_expresion(expresion[:posicion]) and validar_expresion(expresion[posicion +1 :])

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           