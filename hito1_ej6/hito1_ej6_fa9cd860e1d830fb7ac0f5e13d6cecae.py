#Ordenar tres números
l = []
x = int(input("Ingresa el primero numero: "))
y = int(input("Ingresa el segundo numero: "))
z = int(input("Ingresa el tercer numero: "))

l.append(x)
l.append(y)
l.append(z)

list.sort(l)

print(str(l[0]) + ", " + str(l[1]) + ", " + str(l[2]))