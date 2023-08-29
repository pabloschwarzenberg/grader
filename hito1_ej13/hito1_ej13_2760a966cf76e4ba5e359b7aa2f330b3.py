#Factores Primos
def es_primo(numero):
  divisor = 2
  c = 0
  if numero == 1:
    return False
  while divisor < numero:
    if numero % divisor == 0 and c == 0:
      c += 1
      return False
      break
    if numero % divisor != 0 and c == 0:
      divisor += 1
  else:
    return True

n = int(input("Ingrese número:"))
x = 1
while x <= n:
  if es_primo(x) and n % x == 0:
    print(str(x))
  x += 1     