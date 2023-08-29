def validar_expresion(expresion):
    if len(expresion)<=1:
      return expresion in "+-"
    if expresion[-1].isdigit() and expresion[0].isdigit():
      return validar_expresion(expresion[1:-1])
    else:
      return False
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           