#Factores Primos
def es_primo(numero):
    divisor=2
    if numero==1 or numero==0:
        return False
    if numero==2:
        return True
    while divisor<numero:
        if numero%divisor==0:
            return False
        divisor+=1
    return True       
           
numero=int(input())
divisor=2
lista=[]
while divisor<=numero:
    if numero==2:
        print(2)
    if es_primo(divisor)==True and numero!=2:
        if numero%divisor==0:
            print(divisor)
    divisor+=1
