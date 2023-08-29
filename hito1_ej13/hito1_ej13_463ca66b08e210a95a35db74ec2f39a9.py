i=2
n=int(input('Ingrese numero: '))
while i<=n:
    while n%i==0:
        n=n/i
        print(i)
    i+=1