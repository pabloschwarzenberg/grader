#Ordenar tres números
print("ordenbar el numero de mayor a menor")

x =eval(input("ingrese un numero:"))
y =eval(input("ingresar un segunmdo numero:"))
z =eval(input("ingresar un tercer numero:"))
        
ma =max(x,y,z)
print("el numero mayor es:",ma)
mi =min(x,y,z)
print("el numero menor es:",mi)

d=(x+y+z)-ma-mi

print("de menor a mayor el orden es",mi,",",d,",",ma)