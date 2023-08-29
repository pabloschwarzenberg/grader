def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    
    if suma == 1:
        return f"El número {a} es primo."
    else:
        return f"El número {a} no es primo. La suma de sus divisores es {suma}."
print(suma_divisores(7))
print(suma_divisores(12))
           