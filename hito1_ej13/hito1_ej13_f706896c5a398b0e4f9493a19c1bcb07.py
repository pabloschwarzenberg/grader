#Factores Primos
def es_primo(numero) :
    j=2
    if numero==1 :
        return False
    if numero==2 :
        return True
    for i in range(numero) :
        d=numero%j
        j+=1
        if d==0 :
            return False
        if j==numero :
            return True
n=int(input("Ingrese numero: "))
y=1

for t in range(n) :
    if n%y==0 :
        if es_primo(y)==True :
            print(y)           
    y+=1