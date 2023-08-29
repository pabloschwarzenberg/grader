def numero_perfecto(n):
  contador=1
  suma=0
  while contador!=n:
    if n%contador==0:
      suma=suma+contador
    contador=contador+1
  if suma==n:
    return True
  else:
    return False


  x=eval(input("Ingrese su numero"))
  if numero_perfecto(n):
    print("el numero {0} si es perfecto".format(n))
  else:
    print("el numero {0} no es perfecto".format(n))