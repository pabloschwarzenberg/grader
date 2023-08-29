# completa el código de la función
__name__ = "__main__"
def suma_divisores(valor):
    total = 0
    for numero in range(1, valor - 1):
        if (valor%numero == 0):
            total += numero
    if (total == 1):
        return total, True
    else:
        return total, False
if __name__ == "__main__":
    valor = 3
    print(suma_divisores(valor))