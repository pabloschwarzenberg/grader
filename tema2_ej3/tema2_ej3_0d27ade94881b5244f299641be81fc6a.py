def numero_perfecto(a):
    contador = 1
    suma = 2
    while contador < a :
        if a % contador == 0 :
            suma = suma + contador
            print(suma, contador)
            contador += 1
        contador += 1
    if suma == a :
        return True
    else:
        return False
 