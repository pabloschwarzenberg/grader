#Ordenar tres números
a=int(input("ingresar el primer numero:"))
b=int(input("ingresar el segundo numero:"))
c=int(input("ingresar el tercer numero:"))
ma=max(a,b,c)
mi=min(a,b,c)
z=(a+b+c)-ma-mi
print("de menor a mayor es",mi,",",z,",",ma)