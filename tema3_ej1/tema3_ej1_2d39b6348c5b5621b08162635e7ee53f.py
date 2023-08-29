def suma_divisores(n):
  divisores = []
  for i in range(1, n):
    if n % i ==0:
      divisores.append(i)
  return sum(divisores)

def primo(n):
  for i in range(1, n+1):
    if n % i == 0:
      return False
  return True            


if __name__=="__main__":
  n=int(input("Ingrese n: "))
  print (suma_divisores(n), primo(n))
