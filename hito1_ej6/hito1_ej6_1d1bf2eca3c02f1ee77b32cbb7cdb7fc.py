#Ordenar tres números
x=eval(input("Ingrese un numero: "))   
y=eval(input("Ingrese un segundo numero: "))
z=eval(input("Ingrese un tercer numero: "))
nmayor=max(x,y,z)
print("el numero mayor es: ", nmayor)
nmenor=min(x,y,z)
print("el numero menor es: ",nmenor)
nmedio=(x+y+z)-nmenor-nmayor
print("De menor a mayor el orden es ",nmenor,",",nmedio,",",nmayor)