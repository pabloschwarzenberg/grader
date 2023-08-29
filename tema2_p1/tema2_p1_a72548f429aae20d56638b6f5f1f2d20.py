#Escribe una función llamada es_primo que retorne True cuando un número es primo y False cuando no lo es.numero = eval(input("Ingrese un número"))def primo(num):
def esPrimo(x):
    numero = int(x)
    esPrimo = True
    if numero == 1:
        esPrimo = False
    for i in range(1, numero):
        if numero % i == 0:
            if i != 1:
                esPrimo = False
                return esPrimo
    return esPrimo