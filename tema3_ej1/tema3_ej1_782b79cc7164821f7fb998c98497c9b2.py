# completa el código de la función
def suma_divisores(a):
  for i in range(1,a):
    if (a%2) ==0:
      return print(True)
    else:
      suma=0
      suma=suma+i
      print(suma)
      return print(False)
n=int(input('Ingrese su numero: '))
suma_divisores(n)
           