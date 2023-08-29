def son_amigos(a, b):
    def suma_divisores(num):
        suma = 0
        for i in range(1, num):
            if num % i == 0:
                suma += i
        return suma
    
    suma_a = suma_divisores(a)
    suma_b = suma_divisores(b)
    
    return suma_a == b and suma_b == a

# Ejemplos de uso
print(son_amigos(220, 284))  # True, 220 y 284 son números amigos
print(son_amigos(1184, 1210))  # True, 1184 y 1210 son números amigos
print(son_amigos(220, 221))  # False, 220 y 221 no son números amigos

           