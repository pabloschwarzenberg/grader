# completa el código de la función
def suma_divisores(num):
    suma = 0
    for i in range(1,num):
        if num % i == 0:
            suma += i
    if suma == 1:
        return suma, True
    else:
        return suma, False
if __name__ == "main":
    num = int(input("Ingresa un número: "))
    suma, es_primo = suma_divisores(num)
    print("La suma de los divisores de", num, "es:", suma)
    if es_primo:
        print(num, "es un número primo")
    else:
        print(num, "no es un número primo")