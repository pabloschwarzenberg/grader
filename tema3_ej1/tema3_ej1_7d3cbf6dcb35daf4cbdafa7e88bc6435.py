# completa el código de la función
def suma_divisores(a):
  divisores=[]
  suma = 0
  
  for i in range(1,a):
    if a % i == 0:
      divisores.append(i)
    
  for i in divisores:
    suma = suma + i
  
  if suma == 1:
    b = True
  else:
    b=False
    
  return(suma, b)       