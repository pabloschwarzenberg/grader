#Ordenar tres números
x = int(input("escriba el primer numero: "))
y = int(input("escriba el segundo numero: "))
z = int(input("escriba el tercer numero: "))

a = min (x, y, z)
c = max (x, y, z)
b = (x + y + z) - a - c

print("los numeros ordenados son: {}, {}, {}". format(a,b,c) )
      