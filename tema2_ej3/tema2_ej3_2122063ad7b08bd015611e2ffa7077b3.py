def numero_perfecto(numero):
    suma_divisores = sum(divisor for divisor in range(1, numero) if numero % divisor == 0)
    return suma_divisores == numero

if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    if numero_perfecto(a):
        print("El número es perfecto")
    else:
        print("El número no es perfecto")
