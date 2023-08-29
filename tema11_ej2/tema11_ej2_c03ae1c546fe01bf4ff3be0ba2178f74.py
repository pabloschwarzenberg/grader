def validar_expresion(expresion):
  if len(expresion) == 0:
    return True
  if expresion[0] == "+" or expresion[0] == "-":
    expresion = expresion[1:]
    if expresion == "" or expresion[0] == "+" or expresion[0] == "-":
      return False
    else:
      validar_expresion(expresion[1:])
  else:
    validar_expresion(expresion[1:])
  return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           