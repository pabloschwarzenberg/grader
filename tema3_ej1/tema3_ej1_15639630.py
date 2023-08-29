# completa el código de la función
def suma_divisores(a):
  suma=0
  for i in range(1,a):
    if (a%i==0):
      suma=suma+i
  return suma, suma==1
if __name__=='__main__':
  h=int(input('ingrese un numero'))
  t=suma_divisores(h)
  if t==1:
    print('el mumero es primo')
  else:
    print('la suma de los divisores es: ',t)