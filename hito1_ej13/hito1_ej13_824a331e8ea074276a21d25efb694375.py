#Factores Primos
num = int(input("ingresa un numero: "))
X = 2
while X <= num:
  if num%X == 0:
    print(X)
    num = num / X
  else:
    X= X + 1 
