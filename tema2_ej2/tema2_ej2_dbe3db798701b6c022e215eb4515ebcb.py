# completa el código de la función
def amigos(a, b):
    # Función para obtener la suma de los divisores de un número
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma
    

    # Verificar si la suma de los divisores de 'a' es igual a 'b' y viceversa
    if suma_divisores(a) == b and suma_divisores(b) == a:
        return True
    else:
        return False