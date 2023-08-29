# completa el código de la función
def suma_divisores(a):
  suma = 0
  for div in range(1, a + 1):
      if (a % div) == 0:
         suma = suma + div
  suma = suma - a
  if suma == 1:
      return suma, True
  else:
      return suma, False
if __name__ == "__main__":
  num = int(input("Ingrese su numero: "))
  print(suma_divisores(num))