#Factores Primos
n=int(input("numero:"))
factores=[]
i=2
while n>1:
    if n%i==0:
        factores.append(i)
        n=n//i
    else:
        i+=1
for i in factores:
    print(i)
