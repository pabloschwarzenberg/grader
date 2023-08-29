#Ordenar tres números
a = int(input("escribe el primer números: "))
b = int(input("escribe el segundo números: "))
c = int(input("escribe el tercer  números: "))

x = min(a,b,c)
y = max(a,b,c)
z = (a+b+c)-x-y

print(str(x)+ "," + str(z) + "," + str(y))
