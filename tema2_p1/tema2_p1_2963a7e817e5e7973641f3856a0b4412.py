# por favor escribe aquí tu función
def es_primo(numero):
  if numero >1:
    z=0
    divisor=2
    while divisor<numero:
      resto = numero%divisor
      if resto==0:
        z+=1
      divisor+=1
    if z==0:
      return True
    else:
      return False
  else:
    return False
try:
  numero_ingreso = int(input("Ingrese número: "))
  print(es_primo(numero_ingreso))
except:
  print("Ingrese sólo número por favor")
           