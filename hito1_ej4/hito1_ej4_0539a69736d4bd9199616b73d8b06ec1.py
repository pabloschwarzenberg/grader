def A(a):
    b = ""
    while a // 2 != 0:
        b = str(a % 2) + b
        a = a // 2
    return str(a) + b

a = int(input('Introduce el número a convertir a binario: '))
C = (A(a))
print("Resultado=", C)
