#Ordenar tres números
x = int(input("Escribe el numero 1: "))
y = int(input("Escribe el numero 2: "))
z = int(input("Escribe el numero 3: "))

if x < y and x < z and y < z:
    print (x,",",y,",",z)

elif x < y and x < z and z < y:
    print (x,",",z,",",y)

elif y < x and y < z and x < z:
    print (y,",",x,",",z)

elif y < x and y < z and z < x:
    print (y,",",z,",",x)

elif z < x and z < y and x < y:
    print (z,",",x,",",y)

elif z < x and z < y and y < x:
    print (z,",",y,",",x)

elif x == y and z > x:
    print (x,",",y,",",z)

elif x == y and z < x:
    print (z,",",x,",",y)

elif x == z and x < y:
    print (x,",",z,",",y)

elif x == z and x > y:
    print (y,",",x,",",z)

elif y == z and x < y:
    print (x,",",y,",",z)

elif y == z and x > y:
    print (y,",",z,",",x)