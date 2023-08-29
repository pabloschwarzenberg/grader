def numero_perfecto(a):
    cantidad_numeros_primos=0
    sumatoria=0
    for i in range(a-1, 0, -1):
        if a % i == 0:
            sumatoria += i
            cantidad_numeros_primos += 1
            print(sumatoria)
    if sumatoria==a:
        return True
    else:
        return False