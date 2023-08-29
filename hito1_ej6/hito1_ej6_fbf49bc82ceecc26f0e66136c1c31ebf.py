#Ordenar tres números
x = str(input("ingrese numero"))
y = str(input("ingrese numero"))
z = str(input("ingrese numero"))

if x <= y and x <= z:
    #x primero
    if y <= z:
        print(x,y,z,sep=",")
    else:
        print(x,z,y,sep=",")
if y <= x and y <= z:
    #y primero
    if x <= z:
        print(y,x,z,sep=",")
    else:
        print(y,z,x,sep=",")

if z <= x and z <= y:
    #z primero
    if x <= y:
        print(z,x,y,sep=",")
    else:
        print(z,y,x,sep=",")
