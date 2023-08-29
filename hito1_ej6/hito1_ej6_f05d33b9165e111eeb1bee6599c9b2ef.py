x=int(input("introduzca el primer numero: "))
y=int(input("introduzca el sugundo numero: "))
z=int(input("introduzca el tercer numero: "))

menor= min(x,y,z)
mayor= max(x,y,z)
intermedio = x+y+z - (menor+mayor)

print("el orden es: {},{},{}".format(menor,intermedio,mayor))