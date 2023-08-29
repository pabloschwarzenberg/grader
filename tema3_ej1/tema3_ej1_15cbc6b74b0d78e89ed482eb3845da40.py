# completa el código de la función
def suma_divisores(a):
    f =[]
    for i in range(1, a):
        if a % i == 0:
            f.append(i)
    f=sum(f)
    if f == 1:
        return f, True
    else:
        return f, False
    return 
    a = int(input("ingrese el numero deseado: "))
    r=suma_divisores(a)
    print(r)