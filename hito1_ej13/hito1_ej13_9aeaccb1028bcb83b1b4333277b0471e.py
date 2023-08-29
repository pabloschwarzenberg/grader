#Factores Primos
nmb=int(input("Ingrese algun numero:"))
n=2
while n<=nmb:
    if nmb % n==0:
       print(n)
       nmb=nmb/n
    else:
       n+=1