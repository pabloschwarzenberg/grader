
numero_a_procesar = int(input())


def factorizar(numero_a_procesar):
    nums_primos = iter((2, 3, 5, 7, 11, 13, 17, 19, 23, 29))
    primo_activo = next(nums_primos)
    x = None
    
    while x != 1:
        if numero_a_procesar % primo_activo != 0:
            primo_activo = next(nums_primos)
            continue
        print(primo_activo)
        numero_a_procesar = x = numero_a_procesar/primo_activo

factorizar(numero_a_procesar)
     