#Factores Primos
def es_primo(numero):
  primacidad = False
  contador = 0
  for i in range(numero):
    division = numero%(i+1)
    if division == 0:
      contador += 1
    if contador == 2:
      primacidad = True
    elif contador != 2:
      primacidad = False
  return primacidad

def divisores(num):
  suma = 0
  for i in range(num):
    try:
      if num%(i+1) == 0:
        if i+1 != 1 and es_primo(i+1):
          print(i+1)
    except:
      dividedByZero = True

divisores(int(input()))