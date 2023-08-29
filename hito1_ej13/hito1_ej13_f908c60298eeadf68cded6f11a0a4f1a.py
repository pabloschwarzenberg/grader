x = int(2)
y = int(input("Ingrese el numero: "))
while(y != 1):
    if (y % x == 0 ):
        print(str(x) + "") #str se utiliza para representar texto, más conocido en el mundo de la programación como string o cadena de caractere
        y = y / x
    else:
        x = x + 1