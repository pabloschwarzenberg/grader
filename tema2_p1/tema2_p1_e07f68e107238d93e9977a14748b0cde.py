def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma, suma == 1

 if _name_ == "_main_":
    numero = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(numero)
    print("La suma de los divisores de {} es: {}".format(numero, suma))
    print("El número {} es primo: {}".format(numero, es_primo))
           