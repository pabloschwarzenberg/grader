# completa el código de la función
def suma_divisores(a):
  contadorNE = 0
  if a == 1:
    return (0,False)
  else:  
    for i in range(1,a):
      if a % i == 0:
        contadorNE += i
    if contadorNE == 1:
      return (contadorNE,True)    
    else:
      return (contadorNE,False)  

if __name__=="__main__":
  a = int(input())
  print(suma_divisores(a))  