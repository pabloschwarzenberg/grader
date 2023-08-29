#a = int(input("Ingresa a: "))
#b = int(input("Ingresa b: "))
def suma_divisores_a(a):
    divisores = [1]
    for i in range(2, a + 1):
        if a % i == 0:
            divisores.append(i)
    return sum(divisores)
resultado_a = (suma_divisores_a)

#b = int(input("Ingresa b: "))
def suma_divisores_b(b):
    divisores = [1]
    for i in range(2, b + 1):
        if b % i == 0:
            divisores.append(i)
    return sum(divisores)
resultado_b = (suma_divisores_a)
if resultado_a == suma_divisores_b or resultado_b == suma_divisores_a:
    print('True')
else:
    print('False')