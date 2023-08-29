#Ordenar tres números
x = int(input("Ingrese el primer valor: "))

y = int(input("Ingrese el segundo valor: "))

z = int(input("Ingrese el tercer valor: "))


a = min(x,y,z)

b = max(x,y,z)

c = (x + y + z) - a - b

print("De menor a mayor el órden es ", a ," , ", c , " , ", b)