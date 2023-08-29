# completa el código de la función
def suma_divisores(a):
    suma = 0
    primo = True
    for i in range(1, a):
        if a % i == 0:
            suma = suma + i
    if suma != 1:
        primo = False
    elif suma == 1:
        primo = True

    return suma, primo

if __name__ == "__main__":
  n = int(input('ingrese el numero: '))
  suma_divisores(n)