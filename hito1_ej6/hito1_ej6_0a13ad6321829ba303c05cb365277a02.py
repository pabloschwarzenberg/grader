#Ordenar tres números
x = int(input("Escriba el primer digito"))
y = int(input("Escriba el segundo digito"))
z = int(input("Escriba el tercer digito"))

a =min(x, y, z)
c =max(x, y, z)
b = (x + y + z) - a - c

print("los numeros de menos a mayor son ", (a, b , c))  