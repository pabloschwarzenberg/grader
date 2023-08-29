def validar_expresion(expresion):
    if expresion == (2 + 3) or (2 - 3):
        return True
    try:
        expresion == 2++
        expresion == --2
        expresion == 2-
    except:
        return False

validar_expresion(expresion)
print(validar_expresion("2+3"))
print(validar_expresion("2-3"))
print(validar_expresion("2++"))
print(validar_expresion("--2"))
print(validar_expresion("2-"))
           