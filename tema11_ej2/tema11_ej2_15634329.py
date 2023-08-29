def validar_expresion(expresion):
  l=["-","+"]
  L=["1","2","3","4","5","6","7","8","9","0"]
  if len(expresion)==1 and l.count(expresion)==1:
    return False
  elif len(expresion)==1 and L.count(expresion)==1:
    return True
  if l.count(expresion[0])==1 and l.count(expresion[1])==1:
    return False
  else:
    return validar_expresion(expresion[1:])

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           