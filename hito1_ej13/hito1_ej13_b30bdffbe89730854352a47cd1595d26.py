#Factores Primos
def es_primo(numero):
    if numero<=1:
        return(False)
    contador=0
    for i in range(2,numero-2):
        if numero%i==0:
            contador=contador+1
    if contador>0:
        return(False)
    return(True)
primos=[]
for i in range(1000):
    if es_primo(i):
        primos.append(i)
def divisores(num):
    while(num>1):
        for i in range(1,num+1):
            if num%i==0 and i in primos:
                print(i)
                num=int(num/i)

num=int(input("ingrese un número entero: "))
divisores(num)
    