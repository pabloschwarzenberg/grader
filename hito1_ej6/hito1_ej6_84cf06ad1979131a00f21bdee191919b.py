x = int(input("Escriba primer numero: "))
y = int(input("Escriba segundo numero: "))
z = int(input("Escriba tercer numero: "))

a = min(x ,y , z)
c = max(x , y, z)
b = (x + y + z) - a - c

print("Los numeros ordenados es: {}, {} , {}".format(a, b , c))