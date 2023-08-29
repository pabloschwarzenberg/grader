def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma

def es_primo(numero):
    if suma_divisores(numero) == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    num = int(input("Ingrese un número: "))
    print("La suma de los divisores es:", suma_divisores(num))
    if es_primo(num):
        print("El número", num, "es primo")
    else:
        print("El número", num, "no es primo")
