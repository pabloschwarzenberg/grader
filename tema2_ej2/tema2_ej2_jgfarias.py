# completa el código de la función
def amigos():
    a=int(input("Ingrese el primer termino: "))
    suma_a=0
    for i in range(1,a):
        if a%i==0:
            suma_a=suma_a+i
    print(suma_a)

    b=int(input("Ingrese el segundo termino: "))
    suma_b=0
    for j in range(1,b):
        if b%j==0:
            suma_b=suma_b+j
    print(suma_b)

    if ((suma_a==b) or (suma_b==a)):
        print("Amigos")
    elif((suma_a!=b)or(suma_b!=a)):
        print("No amigos")

amigos()           