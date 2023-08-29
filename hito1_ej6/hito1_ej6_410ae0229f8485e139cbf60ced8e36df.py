#Ordenar tres números
x=int(input("ingresa: "))
y=int(input("ingresa: "))
z=int(input("ingresa: "))
if x<y and x<z:
    if y<z:
        print("ordenados son: ",(x,y,z))
    else:
        print("ordenados son: ",(x,z,y))
elif y<x and y<z:
    if x<z:
        print("ordenados son: ",(y,x,z))
    else:
        print("ordenados son: ",(y,z,x))
else:
    if x<y:
        print("ordenados son: ",(z,x,y))
    else:
        print("ordenados son: ",(z,y,x))
  