#Factores Primos
n = int(input("ingrese numero:" ))
sep = ","
primos = []

for i in range(2, n+1):
    while n%i == 0:
        primos.append(i)
        n = n/i
      

primos1 = [str(item) for item in primos]

for i in primos1:
    print(i, end="\n")

