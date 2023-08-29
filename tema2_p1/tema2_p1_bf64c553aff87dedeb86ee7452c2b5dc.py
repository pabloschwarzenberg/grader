# por favor escribe aquí tu función
def es_positivo(n):
  if n > 0:
    return True
  else:
    return False

def es_primo(n):
  for i in range(2,n):
    if n % i == 0:
      return False
  return True
numero = int(input("Ingrese el numero: "))
if es_positivo(numero):
  if es_primo(numero):
    print("Es un numero primo")
  else:
    print("No es un numero primo")
else:
  print("Ingreso un numero menor o igual que 0")
 
  
  
                 