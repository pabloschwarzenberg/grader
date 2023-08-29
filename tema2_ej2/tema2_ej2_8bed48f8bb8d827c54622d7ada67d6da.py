# completa el código de la función
def amigos(a, b):
    # Función para calcular la suma de los divisores de un número
    def suma_divisores(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma

    # Verificar si a y b son números amigos
    suma_div_a = suma_divisores(a)
    suma_div_b = suma_divisores(b)

    if suma_div_a == b and suma_div_b == a:
        return True
    else:
        return False
        
           