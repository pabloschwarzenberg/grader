# por favor escribe aquí tu función
def es_primo(numero):
if numero >1:
a = 0
divisor = 2
while divisor<numero:
resto = numero%divisor
if resto == 0:
a+ = 1
divisor+ = 1
if a==0:
return true
else:
  return false
  else:
  return false
  try:
  numero_ingreso = int(input("ingrese numero:"))
  print(es_primo(numero_ingreso))
  except:
  print("ingrese solo numeropor favor")
  
           