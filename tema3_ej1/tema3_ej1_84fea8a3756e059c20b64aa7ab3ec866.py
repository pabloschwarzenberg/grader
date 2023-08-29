# completa el código de la función
def suma_divisores(a):
  divisores = [0]

  for i in range(1,a-1):
      if a % i==0:
          divisores.append(i)
  s = sum(divisores)
  if s==1:
     return (s,True)
  else:
     return (s,False)

if __name__ == "__main__":
  num = int(input("Ingrese un numero: "))
  solucion = suma_divisores(num)
  print(solucion)
  
  