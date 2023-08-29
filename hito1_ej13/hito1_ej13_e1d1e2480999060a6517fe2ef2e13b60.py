def factor_primo(numero):
    i = 2
    while i <= numero:
        if numero % i == 0:
            print(i)
            numero = numero / i
        else:
            i = i + 1
numero = int(input("Ingrese un número entero: "))

if numero <= 0:
    print("El número debe ser positivo.")
else:
    print("Factores primos de", numero, ":")
    factor_primo(numero)      