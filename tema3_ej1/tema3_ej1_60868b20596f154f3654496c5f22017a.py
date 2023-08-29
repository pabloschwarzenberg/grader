# completa el código de la función
def suma_divisores(n):
    n = abs(n)

    def _sumar_divisores(div_actual):
        if div_actual == 0:
            return 0

        s = _sumar_divisores(div_actual - 1)

        if n % div_actual == 0:
            return s + div_actual

        return s

    return _sumar_divisores(n)

print(suma_divisores(1))  