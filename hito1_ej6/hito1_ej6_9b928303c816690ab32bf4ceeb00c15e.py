#Ordenar tres números
x = input("Ingrese un número: ")
y = input("Ingrese un número: ")
z = input("Ingrese un número: ")

if x<=y<=z:
        print("El orden es: ",(x), ",", (y), ",", (z))
elif x<=z<=y:
        print("El orden es: ",(x), ",", (z), ",", (y))
elif y<=z<=x:
        print("El orden es: ",(y), ",", (z), ",", (x))
elif y<=x<=z:
        print("El orden es: ",(y), ",", (x), ",", (z))
elif z<=x<=y:
        print("El orden es: ",(z), ",", (x), ",", (y))
elif z<=y<=x:
        print("El orden es: ",(z), ",", (y), ",", (x))
