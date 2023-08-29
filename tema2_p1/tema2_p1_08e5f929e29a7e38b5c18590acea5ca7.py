# por favor escribe aquí tu función
def es_primo(numero):
  if numero<2:
        return False
  for i in range(2,numero):
      if numero%i == 0:
          return False
      return True
if __name__ == "__main__":
  numero = int(input())
  print(es_primo(numero))
           