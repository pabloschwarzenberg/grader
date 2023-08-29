#Ordenar tres números
x = int(input("ingrese un número porfavor"))
y = int(input("ingrese un número porfavor"))
z = int(input("ingrese un número porfavor"))

Menor = min(x , y , z)
Mayor = max(x , y , z)

resultado = (x + y + z) - Mayor - Menor

print("el orden de los digitios de menor a mayor es: ", Menor, " , " , resultado, ", " , Mayor) 