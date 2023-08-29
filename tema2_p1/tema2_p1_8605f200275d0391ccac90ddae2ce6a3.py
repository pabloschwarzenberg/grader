# por favor escribe aquí tu función
def es_primo(n):
  for i in range(2,n):
    if (n%i) == 0:
      return print(False)
  return print(True)
n=int(input())
es_primo(n)
           