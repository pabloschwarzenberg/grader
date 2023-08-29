def validar_expresion(expresion):
  numeros=["0","1","2","3","4","5","6","7","8","9"]
  lista=[]
  contador=0
  lista=list(expresion)
  for i in lista:
      if i not in numeros:
          contador+=1
      if i in numeros:
          contador=0
      if contador>1:
          return False
  if expresion[len(expresion)-1] not in numeros:
      return False
  return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           