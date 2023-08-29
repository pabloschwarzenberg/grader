#Factores Primos
numero=int(input("Numero: "))
primos=[]
for i in range(2, numero+1):
    while numero%i==0:
        primos.append(i)
        numero=numero/i
for elem in primos:
    print(elem)