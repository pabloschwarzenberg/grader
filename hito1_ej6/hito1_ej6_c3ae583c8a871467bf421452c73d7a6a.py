#Ordenar tres números
x=int(input("ingrese un numero:"))
y=int(input("ingrese el segundo numero:"))
z=int(input("ingrese un numero:"))
mi= min(x,y,z)
ma= max(x,y,z)
mid= (x+y+z)- (mi + ma)
print(mi,",",mid,",",ma)