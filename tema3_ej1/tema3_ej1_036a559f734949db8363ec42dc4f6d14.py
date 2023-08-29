# completa el código de la función
def suma_divisiones(n):
  divisores = []
  for i in range(1,n):
    if n%i == 0:
      i = divisores.append(i)
      suma=0
      for divisor in divisores:
        suma = suma + divisor
        if suma==1:
          es_primo= True
          return suma, es_primo
        else:
          es_primo = False
          return suma, es_primo
           