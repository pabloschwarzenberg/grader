operadores = ["+","-"]

def validar_expresion(expresion):
  q = len(expresion)-1
  for x in operadores:
    if expresion[0] == x:
      return False
  for x in operadores:
    if expresion[q] == x:
      return False
  i=0
  while i<len(expresion)-1:

      if expresion[i]==expresion[i+1]:
          return False
      else:
          i+=1
  return True



if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           