#Ordenar tres números
x=int(input("ingrese primer numero:"))
y=int(input("ingrese segundo numero:"))
z=int(input("ingrese tercer numero:"))
ma=max(x,y,z)
mi=min(x,y,z)
d=(x+y+z)-(ma+mi)
print("el orden de menor a mayor es",mi,",",d,",",ma)