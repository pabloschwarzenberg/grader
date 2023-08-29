def numero_perfecto(x):
    divisores = []
    for j in range(1, x):
        if (x % j) == 0:
            j = divisores.append(j)
    total = 0
    for d in divisores:
        total = total + d
    if (total == x):
        perfecto = True
    else:
        perfecto = False
    return perfecto
if __name__=="__main__":
    y = int(input("Porfavor, coloque y: "))
    print(numero_perfecto(a))