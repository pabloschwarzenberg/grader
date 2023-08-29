#Factores Primos
def es_primo(numero):
    c=0
    for x in range(2,numero+1):
        if numero%x==0:
           c+=x
    if c==numero:
        return True
    else:
        return False
n=int(input(":"))
for x in range(2,n+1):
     if n%x==0 and es_primo(x):
        print(x)