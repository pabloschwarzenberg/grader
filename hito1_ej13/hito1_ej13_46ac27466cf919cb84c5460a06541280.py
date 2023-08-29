#Factores Primos
def es_primo(numero):
  NumeroI = numero
  Divisor = 2
  I = 0
  Numero = 0
  while I < NumeroI:
    Numero = NumeroI / Divisor
    Numero2 = NumeroI // Divisor
    I += 1
    Divisor += 1
    if numero == 1:
      NumeroI = False
      break
    elif Numero == 1.0:
      NumeroI = True
      break
    elif Numero == float(Numero2):
      NumeroI = False
      break
  return NumeroI

numero_entero = int(input('Ingrese numero'))
c = 0
d = 0
factores = 1
while factores < numero_entero:
  c += 1
  numero = c
  numero1 = numero_entero / c
  numero2 = numero_entero // c
  if numero1 == float(numero2):
    factor = es_primo(numero)
    if factor == True:
      print(numero)
      factores *= numero
    elif factores == numero_entero:
      break
    elif c == numero_entero:
        c = 0
       