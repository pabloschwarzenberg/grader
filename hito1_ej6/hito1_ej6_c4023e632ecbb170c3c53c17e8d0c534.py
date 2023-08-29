#Ordenar tres números
x = int(input("Escriba el primer numero: "))
y = int(input("Ecriba el segundo numero: "))
z = int(input("Escriba el tercer numero: "))

min = min(x,y,z)
max = max(x,y,z)
med = (x + y + z) - min - max

print("Los numeros ordenados de menos a mayor es: {}, {}, {} ".format(min, med, max))