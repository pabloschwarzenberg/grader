def validar_expresion(expresion):
  if len(expresion)==1:
    if expresion.isdigit():
      return True
    else:
      return False
  if expresion[0].isdigit():
    return validar_expresion(expresion[1:len(expresion)])                        
  else:
    if expresion[1].isdigit():
      return validar_expresion(expresion[1:len(expresion)])
    else:
      return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           