#Ordenar tres números
a = int(input("Escriba el primer número: "))
b = int(input("Escriba el segundo número: "))
c = int(input("Escriba el tercer número: "))

x = min(a,b,c)
y = max(a,b,c)
z = (a+b+c)-x-y

print("Los números son :", (x,z,y)) 