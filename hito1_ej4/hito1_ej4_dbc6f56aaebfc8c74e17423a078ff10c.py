n=int(input("Ingrese Un Numero: "))
i=0
bi=0
while(n>0):
    x=n%2
    n=int(n//2)
    bi=bi+x*(10**i)
    i=i+1
print("resultado=",bi)