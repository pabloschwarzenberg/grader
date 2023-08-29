# completa el código de la función
def suma_divisores(k):
    fa =[]
    for i in range(1, k):
        if k % i == 0:
            fa.append(i)
    fa=sum(fa)
    if fa == 1:
        return fa, True
    else:
        return fa, False
    return 
    k = int(input("ingrese el numero deseado: "))
    r=suma_divisores(a)
    print(r)
    