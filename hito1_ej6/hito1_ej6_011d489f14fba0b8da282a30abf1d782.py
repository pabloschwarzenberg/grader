l=int(input("ingrese un numero: "))
a=int(input("ingrese un numero: "))
m=int(input("ingrese un numero: "))
ma=max(l,a,m)
mi=min(l,a,m)
d=(l+a+m)-ma-mi
print("los numeros ordenados de menor a mayor son ",mi,",",d,",",ma)