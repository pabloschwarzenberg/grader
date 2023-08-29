def numero_perfecto(a):
    esPerfecto = False
    i = 1
    divisores = []
    while i < a:
        if a%i == 0:
            divisores.append(i)
            i += 1
        else:
            i += 1
    suma = sum(divisores)
    if suma == a:
        esPerfecto = True
        return esPerfecto
    else:
        return esPerfecto

           