# completa el código de la función
def suma_divisores(numero):
  lista=list(range(1,numero))
  lista2=[]
  for n in lista:
    if numero%n==0:
      lista2.append(n)
  suma=sum(lista2)
  return suma

def detector_primo(suma,numero):
  if suma==0:
    return False
  lista=list(range(2,suma))
  if suma==2:
    return False
  if suma==1:
    return True
  for n in lista:
    if numero%n==0:
      return False
  return True

if __name__ == "__main__":
  numero=eval(input('numero: '))
  suma=suma_divisores(numero)
  print('(',suma_divisores(numero),',',(detector_primo(suma,numero)),')')