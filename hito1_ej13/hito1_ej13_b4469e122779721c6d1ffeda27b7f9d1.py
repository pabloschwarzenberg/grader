#Factores Primos
def descompone(x):
  N = []
  for y in range(2,x+1):
    while x % y == 0:
      N.append(y)
      x = x / y
  return N
x = int(input("ingresa un numero: "))
X = descompone(x)
for V in X:
  print(V)  
  