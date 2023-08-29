#Factores Primos
num = int(input("Ingrese el numero"))
i = 1
while i<=num:
 if num%i==0 and not(i==1):
  num = num/i
  print(i)
  i = 1
 i = i + 1      