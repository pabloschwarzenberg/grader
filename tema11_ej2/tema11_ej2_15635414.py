def validar_expresion(expresion):
  a=list(expresion)
  operaciones = ["+","-"]
  if len(a) == 3:
    if a[0] == operaciones[0] or a[0] == operaciones[1] or a[2]  == operaciones[0] or  a[2]  == operaciones[1]: 
        return False
    else:
        numero1 = float(a[0])
        numero2 = float(a[2])
    if numero1 == int(numero1) and numero2 == int(numero2):
         if a[1] in operaciones:
             return True
         else:
             return False
    else: 
         return False
  else:
      return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))


           