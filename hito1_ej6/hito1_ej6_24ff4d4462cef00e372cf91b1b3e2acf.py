###Ejercicio 3
print("Los números que introduzcas se ordenaran de menor a mayor")
x= eval(input("Ingrese el primer valor: "))
y= eval(input("Ingrese el segundo valor: "))
z= eval(input("Ingrese el tercer valor: "))

q= min(x,y,z)
w= max(x,y,z)
e= (x+y+z) -q -w

print("Los números son: {},{},{}".format(q,e,w), "ordenados de menor a mayor")
