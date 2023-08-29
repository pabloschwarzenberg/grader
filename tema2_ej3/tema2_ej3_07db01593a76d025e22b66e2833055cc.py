def numero_perfecto(a):
    suma_divisores = 0
    for i in range(1, a):
        if a % i == 0:
            suma_divisores += i

    if suma_divisores == a:
        return True  # El número es perfecto
    else:
        return False  # El número no es perfecto

_name_ = 0
if _name_ == "_main_":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))