def numero_perfecto(numero):
    suma_divisores = sum(divisor for divisor in range(1, numero) if numero % divisor == 0)
    return suma_divisores == numero

if _name_ == "_main_":
    numero = int(input("Ingrese un número: "))
    if numero_perfecto(numero):
        print(numero, "es un número perfecto")
    else:
        print(numero, "no es un número perfecto")