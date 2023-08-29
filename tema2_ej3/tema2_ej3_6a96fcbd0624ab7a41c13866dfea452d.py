def divisores(n):
  divisores = []
  i = 1
  while i < n:
    if n % i == 0:
      divisores.append(i)
    i = i + 1
  return divisores
def numero_perfecto(a):
    if sum(divisores(a)) == a:
      return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           