def numero_perfecto(np):
  contador=1
  suma=0
  while contador!=np:
    if np%contador==0:
      suma=suma+contador
    contador=contador+1
  if suma==np:
    return True
  else:
    return False


  x=eval(input("Ingrese su numero"))
  if numero_perfecto(np):
    print("El numero {0} si es perfecto".format(np))
  else:
    print("El numero {0} no es perfecto".format(np))