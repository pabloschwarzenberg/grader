# completa el código de la función
def suma_divisores(a):
    b = a #usare b como el divisor
    suma = 0 #aqui acumulare la suma de los divisores
  
    while b>1: # ciclo para repetir varias veces el proceso
        b -= 1 #le voy restando 1 a b para que vaya probando con los números menores al indicado
        if a%b == 0: #saco el modulo para ver si es divisible o no
            suma += b #si es divisible le sumo ese número

    if suma == 1: #Si se cumple este if, el número es primo
        return (suma, True)
    else:  #Si no se cumple no es primo
        return (suma,False)