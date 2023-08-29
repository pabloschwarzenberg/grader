def resolver_sistema():
    a1=float(input("Ingrese el valor de a1: "))
    b1=float(input("Ingrese el valor de b1: "))
    c1=float(input("Ingrese el valor de c1: "))
    a2=float(input("Ingrese el valor de a2: "))
    b2=float(input("Ingrese el valor de b2: "))
    c2=float(input("Ingrese el valor de c2: "))
    determinante=a1*b2-a2*b1
    if determinante==0:
        print("El sistema no tiene solucion unica.")
    else:
        x=(b2*c1-b1*c2)/determinante
        y=(a1*c2-a2*c1)/determinante
        print(["x="+str(round(x, 1))])
        print(["y="+str(round(y, 1))])

resolver_sistema()