de= int(input("Ingrese un numero decimal "))
i=0
bi=0
while (de>0):
 di=de%2
 de=int(de//2)
 bi=bi+di*(10**i)
 i=i+1
print("resultado=",bi)