# completa el código de la función
def suma_divisores(n):
    primo = False
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)

        elif n == 1:
            div = []

#    print(div)
    resultado = 0
    longitud = len(div)
    m=0
    for i in div:
        resultado += i

    if longitud == 1:
        primo = True
    elif longitud >= 2:
        primo = False
    elif longitud == 0:
        primo = False

    return (resultado, primo)


if __name__ == "__main__":
    n = int(input("Ingrese un número"))
    sumas = suma_divisores(n)
    print(sumas)

