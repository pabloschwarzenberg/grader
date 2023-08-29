# completa el código de la función
def suma_divisores(a):
  divisores = [i for i in range(1, a + 1) if a % i == 0 and not i == a]
  if sum(divisores) == 1:
    primo = True
  else:
    primo = False
    
  return sum(divisores), primo

if __name__ == "__main__":
  print(suma_divisores(a))
