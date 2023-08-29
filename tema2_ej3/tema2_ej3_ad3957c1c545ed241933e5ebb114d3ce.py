def divisores(x):
  numeros = []
  for i in range (1,x):
    if x % i == 0:
      numeros.append(i)
  return sum(numeros)

def numero_perfecto(a):
  if divisores(a) == a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           