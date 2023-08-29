def suma_divisores(n):
    l=[]
    for i in range (2,n):
        if n%i==0:
            l.append(i)
    return l

def primo(n):
    d=2
    es=True
    while d<=(n**(1/2)) and es:
        es=(n%d!=0)
    if n==1:
        es=False
    if   n==2:
            es=True
    return es
    

n=int(input("Ingresa un numero: "))
l=suma_divisores(n)
if len(l)>0:
    print("El numero",n,"tiene los siguientes divisores:",l)
    l2=[]
    for i in l:
        if primo(i):
            l2.append(i)
    print("De el numero",n,"los divisores primos son: ",l2)

