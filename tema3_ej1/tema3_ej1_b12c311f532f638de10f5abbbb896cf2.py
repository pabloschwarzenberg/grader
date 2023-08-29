# completa el código de la función
def suma_divisores(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    if sum(div) == 1:
        return sum(div), True
    if sum(div) > 1:
        return sum(div), False
    if sum(div) == 0:
        return sum(div), False


if __name__ == "__main__":n = int(input('ingrese un numero: '))
if __name__ == "__main__":print(suma_divisores(n))
