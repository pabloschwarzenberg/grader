#Factores Primos
x = int(2)
n = int(input("Ingrese número a factorizar: "))
while n!=1:
  if n%x==0:
    print(str(x)+" ")
    n = n/x 
  else:
    x = x+1      