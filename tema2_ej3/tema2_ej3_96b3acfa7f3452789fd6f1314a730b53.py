def numero_perfecto(a):
    sa=[]
    for i in range(1, a):
        if a % i == 0:
            sa.append(i)
    sa=sum(sa)
    if sa == a:
        return True
    else:
        return False
    a = int(input("ingrese a: "))
    print(numero_perfecto(a))