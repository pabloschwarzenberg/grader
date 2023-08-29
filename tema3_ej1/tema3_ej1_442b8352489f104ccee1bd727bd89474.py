def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo
#__________________________________-
numero = int(input("Ingrese un numero: "))
suma, es_primo = suma_divisores(numero)
print("La suma de los divisores de numero es:", suma)
if es_primo:
    print(numero,":es primo")
else:
    print(numero, "no es primo")