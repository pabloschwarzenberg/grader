# completa el código de la función
def suma_divisores(a):
  suma=0
  contador=0
  for i in range(1, a+1):
    if a%i==0:
      suma+=i
      contador=contador+1
  if contador==2:
    numero=True
  else:
    numero=False
  return (suma-a, numero)
if __name__=="__main__":
  n=eval(input())
  suma_divisores(n)


           