#Ordenar tres números
x=int(input("Ingrese numero: "))
y=int(input("Ingrese numero: "))
z=int(input("Ingrese numero: "))

if x <= y <= z:
    print("Ordenados")
    print(x,",",y,",",z)
if x <= z <= y:
    print("Ordenados")
    print(x,",",z,",",y)
if y <= x <= z:
    print("Ordenados")
    print(y,",",x,",",z)
if y <= z <= x:
    print("Ordenados")
    print(y,",",z,",",x)
if z <= x <= y:
    print("Ordenados")
    print(z,",",x,",",y)
if z <= y <= x:
    print("Ordenados")
    print(z,",",y,",",x)