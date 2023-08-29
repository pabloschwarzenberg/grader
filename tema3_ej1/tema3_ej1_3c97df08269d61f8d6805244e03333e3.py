# completa el código de la función

def suma_divisores(a):
  divisores = []
  for i in range(1, a):
    if a % i == 0:
      divisores.append(i)

  numero = 0
  for i in range (1, a + 1):
    if a % 1 == 0:
      numero += i

  if numero == 2:
    primo = True
  else:
    primo = False

  return sum(divisores),primo


d = suma_divisores(13)
#if __name__ == "__main__":
print(d)
