def numero_perfecto(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    if sum(divisores) == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input("Ingresa un número: "))
    print(numero_perfecto(num))
