# por favor escribe aquí tu función
def es_primo(numero):
  if numero >1:
    a=0
    div=2
    while div<numero:
      resto = numero%div
      if resto==0:
        a+=1
      div+=1
    if a==0:
      return True
    else:
      return False
  else:
    return False

try:
  numero_ingreso = int(input("icorporar número: "))
  print(es_primo(numero_ingreso))
except:
  print("Ingrese solo numero")