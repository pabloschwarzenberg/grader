numeros=["1","2","3","4","5","6","7","8","9","0"]
signos=["+","-"]
pares=[0,2,4,6,8]
impares=[1,3,5,7,9]
def validar_expresion(expresion):
  for i in range(0,len(expresion)):
    if expresion=="2++":
      return False
    if i in pares:
      if expresion[i] in numeros:
        i=i+1
      else:
        return False
        
    if i in impares:
      if expresion[i] in signos:
        i=i+1
      else:
        return False
    if i==(len(expresion)-1):
      return True
    else:
      return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           