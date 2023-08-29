def numero_perfecto(a):
    sumdiv = 0

    for n in range(1, a):
        if a % n == 0:
            sumdiv += n
    if sumdiv == a:
        return True
    else:
        return False

a = int(input("Ingresa numero: "))
numero_perfecto(a)
           