def numero_perfecto(n):
    listai = []
    for i in range(1, n):
        if (n % i == 0):
            listai.append(i)
    suma = 0
    for i in listai:
        suma += i
        i = i + 1
    if suma == n:
        return True
    elif suma != n:
        return False

