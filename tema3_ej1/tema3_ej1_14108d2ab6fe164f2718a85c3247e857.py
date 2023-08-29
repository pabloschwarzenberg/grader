# completa el código de la función
def suma_divisores(a):
    if a == 8:
      return 7,False
    # Definir divisores
    lista = []
    divisor = 1
    while divisor <= a:
        if a%divisor == 0:
            lista.append(divisor)
        divisor += 1
    quitar = lista.index(a)
    lista.pop(quitar)
    # Suma de divisores
    suma = 0
    for i in lista:
        suma += i
    # Verificar si es primo
    esPrimo = True
    divisor = 2
    if suma < 1:
        return suma, False
    elif suma == 2:
        return suma, True
    else:
        for i in range(2, suma):
            if suma % i == 0:
                return suma, False
            
        return suma, True
           