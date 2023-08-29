#Factores Primos
primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
num=int(input("Ingresa numero:"))
for e in primos:
  if num%e==0:
    print(e)
