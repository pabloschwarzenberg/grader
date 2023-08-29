#Factores Primos
def es_primo(x):
    if x==1:
        return False
    else:
        primo=True
        for i in range(2,x):
          if x%i==0:
            primo=False
        return primo
numero=int(input())
i=1

while i <= numero:
    d=numero%i
    if d==0:
        if es_primo(i)==True:
            print(i)
    i+=1
