def validar_expresion(expresion):
  if expresion[0].isdigit() == False and expresion[1].isdigit() == True:
    if len(expresion) == 2:
      return True
    else:
      return validar_expresion(expresion[1:])
  elif expresion[0].isdigit() == True and len(expresion) > 2:
    return validar_expresion(expresion[1:])
  else:
    return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           