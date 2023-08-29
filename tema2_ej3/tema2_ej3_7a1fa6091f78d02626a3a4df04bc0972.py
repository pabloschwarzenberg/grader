def numero_perfecto(numero):
    suma_divisores = sum([i for i in range(1, numero) if numero % i == 0])
    if suma_divisores == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    print(numero_perfecto(numero))






           