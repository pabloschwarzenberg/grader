#Factores Primos

def es_primo(numero):
  if numero==1 or numero<=0:
      return False
  if numero==2:
      return True
  for i in range(2,numero):
      if numero%i==0:
          return False
  return True


def divisores(numerito,divisor):
    if numerito%divisor==0:
        return True
    else:
        return False


Numero=int(input("Ingrese el número a descomponer: "))

i=1
while i<=Numero:
    if divisores(Numero,i)==True:
        if es_primo(i)==True:
            print(i)
        i+=1
    else:
        i+=1