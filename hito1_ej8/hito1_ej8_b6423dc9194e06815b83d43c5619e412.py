#Descomponer un número
n=int(input("Ingrese 4 digitos: "))
m=n/1000
tmp=n%1000
c=tmp/100
tmp=tmp%100
d=tmp/10
u=tmp%10
print("%iM+"%m,"%iC+"%c,"%iD+"%d,"%iU+"%u)