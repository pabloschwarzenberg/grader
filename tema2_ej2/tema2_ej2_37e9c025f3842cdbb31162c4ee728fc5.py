a = int(input("Ingresa un número: "))
b = int(input("Ingresa otro número: "))
x = 1
suma = 0
while x < a:

    if a % x == 0:

        suma = suma + x

    x = x + 1

if suma == b:
    print("Los números son amigos")

else:
    print("Los números no son amigos")