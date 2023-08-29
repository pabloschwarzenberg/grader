#Ordenar tres números
x = int(input("Ingresa el primer numero: "))
y = int(input("Ingresa el segundo numero: "))
z = int(input("Ingresa el tercer numero: "))

Max = max(x,y,z)
Min = min(x,y,z)

I = (x + y + z) - Max - Min

print(Min, ", ", I , ", ", Max)
