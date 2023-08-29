#Ordenar tres números
 # ordenar de menor a mayor
x = int(input("escriba el numero 1:" ))
y = int(input("escriba el numero 2:" ))
z = int(input("escriba el numero 3:" ))

a = min(x, y, z)
c = max(x, y, z)
b = (x+y+z)-a-c

print("los numeros son: " ,(a, b, c))     