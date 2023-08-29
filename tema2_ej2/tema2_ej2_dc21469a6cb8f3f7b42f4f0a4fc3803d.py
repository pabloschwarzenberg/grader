# completa el código de la función
def amigos(a, b):
    def sumaDivisores(num):
        suma = 0
        for i in range(1, num):
            if num % i == 0:
                suma += i
        return suma
    suma_a = sumaDivisores(a)
    suma_b = sumaDivisores(b)
    return suma_a == b and suma_b == a
# Valores de ejemplo para probar la función
n1 = 220
n2 = 284
resultado = amigos(n1, n2)
print(resultado)