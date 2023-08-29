def numero_perfecto(a):
    f=[]
    for i in range(1, a):
        if a % i == 0:
            f.append(i)
    f=sum(f)
    if f == a:
        return True
    else:
        return False
    a = int(input("ingrese a: "))
    print(numero_perfecto(a))