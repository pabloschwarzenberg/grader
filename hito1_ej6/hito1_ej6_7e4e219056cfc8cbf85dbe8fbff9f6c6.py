#Ordenar tres números
x = int(input("ingrese el primer digito: "))
y = int(input("ingrese el segundo digito: "))
z = int(input("ingrese el tercer digito: "))

a = min(x,y,z)
c = max(x,y,z)
b =(x+y+z)-a-c

print("El orden de menor a mayor es: {}, {}, {},".format(a,b,c))