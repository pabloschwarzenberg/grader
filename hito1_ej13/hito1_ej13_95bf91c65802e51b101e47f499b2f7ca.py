#Factores Primos
def es_primo(numero):
    if numero ==1:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True
    
num=int(input())
for i in range(1,num+1):
    if num%i==0:
       if es_primo(i)== True:
           print (i)