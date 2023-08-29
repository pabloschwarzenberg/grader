def numero_perfecto(var):
  contador=1
  suma=0
  while contador!=var:
    if var%contador==0:
      suma=suma+contador
    contador=contador+1
  if suma==var:
    return True
  else:
    return False

if __name__=="main":
  rabia=eval(input("Ingrese su numero"))
  if numero_perfecto(rabia):
    print("El numero {0} es perfecto".format(rabia))
  else:
    print("El numero {0} no es perfecto".format(rabia))