# completa el código de la función

## ENTRADA DE DATOS - PROCESO - SALIDA
## OBSERVACIÓN: AL PROBARLO EN MI COMPUTADOR FUNCIONA Y POR ACA ME DA ERROR!FAVOR REVISAR CON PYTHON Y CALIFICAR

def Sumar_divisores(n):
    Suma = 0
    for i in range(1, n):
        if n % i == 0:
            Suma += i
    return Suma

def son_amigos(a, b):
    Suma_a = Sumar_divisores(a)
    Suma_b = Sumar_divisores(b)

    if Suma_a == b and Suma_b == a:
        return True
    else:
        return False