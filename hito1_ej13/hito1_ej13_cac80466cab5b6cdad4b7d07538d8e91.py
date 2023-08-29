#Factores Primos
primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
numero=int(input("Ingrese un numero entero y se retornará sus factores primos: "))
factores=[]
for x in range(1,numero+1):
    xd=numero%x
    if xd==0:
        factores.append(x)
for x in factores:
    for a in primos:
        if x==a:
            print(x)
      