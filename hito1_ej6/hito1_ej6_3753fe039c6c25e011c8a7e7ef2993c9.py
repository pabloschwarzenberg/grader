#Ordenar tres números
x=int(input("ingrese su 1er numero: "))
y=int(input("ingrese su 2do numero: "))
z=int(input("ingrese su 3er numero: "))
m=min(x,y,z)
s=max(x,y,z)
w=(x+y+z)-m-s
print("los numeros ordenados de menor a mayor son: {},{},{}".format([m],[w],[s]))    