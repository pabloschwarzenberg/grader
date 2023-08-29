#Ordenar tres números
x = int(input("Ingresa tu primer numero: "))
y = int(input("Ingresa tu segundo numero: "))
z = int(input("Ingresa tu tercer numero: "))
minimo = min(x,y,z)
maximo = max(x,y,z)
medio = ((x + y + z)- minimo - maximo)
print("el orden de los numeros entregados de menor a mayor es: ", minimo ,",", medio ,",", maximo)