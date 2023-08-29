# completa el código de la función
def suma_divisores(a):
    divs = []
    for i in range(1, a):
        if a % i == 0:
            i = divs.append(i)
    suma = 0
    for divisor in divs:
        suma = suma + divisor
    if suma == 1 :
        Primo = True
        return suma, Primo
    else:
        Primo = False
        return suma, Primo
if __name__ == "__main__":
    print(suma_divisores)