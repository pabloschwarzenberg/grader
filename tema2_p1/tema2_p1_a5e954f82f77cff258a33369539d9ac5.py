
# por favor escribe aquí tu función
def es_primo(numero):
  lista=list(range(2,numero))
  if numero==1 or numero==2:
    return False
  for n in lista:
    if numero%n==0:
      return False
  return True

if __name__=="__main__":
  numero=eval(input('numero: '))
  print(es_primo(numero))
