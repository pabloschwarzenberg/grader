# completa el código de la función
def suma_divisores(a):
  divisores = 1
  cont = 0
  primo = False
  for i in range(2,a+1):
    if a%i == 0:
      divisores += i
      cont += 1
  if cont <= 1:
    primo = True
  if a == 0:
    divisores = 0
  if a == 1:
    primo = False
  return divisores-a, primo
  
  if __name__ == "__main__":
    print(suma_divisores(12))
           