# por favor escribe aquí tu función
def es_primo(numero):
  esPrimo=True
  for i in range(2,numero):
    if numero%i==0:
      esPrimo=False
  return esPrimo
n=int(input())
a=es_primo(n)
print(a)