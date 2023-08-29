def numero_perfecto(x):
  contador=1
  suma=0
  while contador!=x:
    if x%contador==0:
      suma=suma+contador
    contador=contador+1
  if suma==x:
    return True
  else:
    return False

if __name__=="__main__":
  x=eval(input("porfavor ingrese su numero"))
  if numero_perfecto(x):
    print("su numero {0} es perfecto".format(x))
  else:
    print("su numero {0} no es perfecto".format(x))