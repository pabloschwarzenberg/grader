#Ordenar tres números

x = int(input("ingrese el primer numeros:"))
y = int(input("ingrese el segundo numeros:"))
z = int(input("ingrese el tercer numeros:"))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

#1,2,3
#a = 1
#c = 3
#b = (1 + 2 + 3) -1 -3
#b = 6 -1 -3 = 2

print("los numeros ordenados son: {},{}, {}".format(a,b,c))