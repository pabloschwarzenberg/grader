n=int(input('ingresa un numero entero: '))
cont=2
while cont<=n:
    if not (n%cont!=0):
        print(cont)
        n/=cont
    else:
        cont+=1