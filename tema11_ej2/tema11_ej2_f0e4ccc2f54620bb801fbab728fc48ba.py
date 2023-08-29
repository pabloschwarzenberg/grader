def validar_expresion(expresion):
    expresion = list(expresion)
    if len(expresion) < 3:
      return False
    try:
      expresion[0] = int(expresion[0])
      expresion[2] = int(expresion[2])
    except ValueError:
      return False
    if type(expresion[1]) == str:
      return True
    else:
      return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           