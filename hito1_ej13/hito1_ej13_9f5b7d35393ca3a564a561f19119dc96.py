#Factores Primos
def es_primo(numero):
    if numero==1 or numero%2==0:
        n=False
    else:
        n=True
    if numero==2:
        n=True
    return n

n=int(input('n: '))
i=2
while i<=n:
    if n%i==0 and es_primo(i)==True:
        n=n//i
        print(i)
    else:
        i=i+1