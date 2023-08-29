def numero_perfecto(a):
    sumita = 0
    for i in range(1, a):
        if a % i == 0:
            sumita += i
    return sumita == a
def lol(a):
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))

