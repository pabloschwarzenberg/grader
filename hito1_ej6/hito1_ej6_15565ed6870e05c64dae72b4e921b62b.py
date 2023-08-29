#Ordenar tres números
a = int(input("escriba el primer número: "))
b = int(input("escriba el segundo número: "))
c = int(input("escriba el tercer número: "))
x = min(a,b,c)
y = max(a,b,c)
z = (a+b+c)-x-y
print("los números son", (x,z,y))