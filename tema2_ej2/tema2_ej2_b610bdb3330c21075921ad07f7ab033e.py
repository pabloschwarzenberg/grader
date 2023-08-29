# completa el código de la función
# completa el código de la función
def amigos(a, b):
    x = 1
    suma = 0
    while x < a:
        if a % x == 0:
            suma = suma + x
        x = x + 1
    if suma == b:
        return True

    else:
        return False

numero_1 = int(input("Ingrese un numeros:"))
numero_2 = int(input("Ingrese otro numeros:"))
print(amigos(numero_1, numero_2))