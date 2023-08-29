#Factores Primos
def es_primo(numero):
    c=0
    if numero==1:
        c=10
    if numero==2:
        c=0
    else:
        for i in range(1,numero):
            if numero%i==0:
                c=c+1
            if numero%i==1:
                c=c
    if c>1:
        return False
    else :
        return True
    
n=int(input("ingrese numero"))
if n==2:
    print("2")
else:
    for numero in range(1,n) :
        if n%numero==0:
            if es_primo(numero)==True :
                print(numero)