numero = int(input("Ingrese un numero: "))
x = int(2)
while numero != 1:
    if numero % x == 0:
        print(x)
        numero /= x
    
    else:
        x += 1