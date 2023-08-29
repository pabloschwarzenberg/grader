def numero_perfecto(a):
  contador = 0
  for divisor in range(1,a-1):
    if (a % divisor) == 0 :
      contador += divisor
   
  if contador==a:
    perfecto  = True
  else:
    perfecto  = False


  return perfecto 

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           