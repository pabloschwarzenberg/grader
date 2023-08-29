x = int(input("Escriba el primer numero: "))
y = int(input("Escriba el segundo numero: "))
z = int(input("Escriba el tercer numero: "))

a = int(min(x, y, z))
c = int(max(x, y, z))
b = int((x + y + z) - a - c)
print("El orden de los numeros es: {}, {} , {}" .format(a, b , c))