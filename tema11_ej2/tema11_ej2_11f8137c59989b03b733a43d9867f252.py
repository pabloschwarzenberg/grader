def validar_expresion(expresion):
  for i in range(0,len(expresion)-1):
    if expresion[i].isdigit()==False and expresion[i+1].isdigit()==False:
      return False
    if expresion[0].isdigit()==False or expresion[len(expresion)-1].isdigit()==False:
      return False
  return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           