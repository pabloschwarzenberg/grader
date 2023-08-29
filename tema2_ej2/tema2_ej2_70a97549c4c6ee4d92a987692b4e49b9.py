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
if __name__ == "__main__":
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    resultado = amigos(n1, n2)
    print(resultado)