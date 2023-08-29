#Ordenar tres números
x=eval(input("Ingrese un numero: "))
y=eval(input("Ingrese un segundo numero: "))
z=eval(input("Ingrese un tercer numero: "))
if x<=y and y<=z:
   print("{},{},{}".format(x,y,z))
elif y<=x and x<=z:
    print("{},{},{}".format(y,x,z))
elif z<=y and y<=x:
    print("{},{},{}".format(z,y,x))
elif z<=x and x<=y:
    print("{},{},{}".format(z,x,y))
elif y<=z and z<=x:
    print("{},{},{}".format(y,z,x))
elif x<=z and z<=y:
    print("{},{},{}".format(x,z,y))