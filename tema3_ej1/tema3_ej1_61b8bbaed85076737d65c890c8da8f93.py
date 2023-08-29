# completa el código de la función
def suma_divisores(a):
 suma = 0
 for numero in range(1,a):
  if a% numero == 0:
   suma = suma + numero
   
 if suma == 1:
  return (suma, True) 
 else:
  return (suma, False)
           