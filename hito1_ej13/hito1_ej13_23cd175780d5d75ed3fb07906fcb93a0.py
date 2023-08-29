#Factores Primos
n=int(input("Ingrese un número a descomponer: "))
primos=[]

for p in range(1,n+1):
    contador=0
    for d in range(1,p+1):
        if(p%d==0):
            contador=contador+1
    if(contador==2):
        primos.append(p)

for div in primos:
    if(n%div==0):
        print(div)    