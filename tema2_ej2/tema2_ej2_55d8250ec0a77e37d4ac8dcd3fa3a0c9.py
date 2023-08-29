# completa el código de la función
def amigos(a, b):
    suma_de_la_letra_a=0
    suma_de_la_letra_b=0
    for i in range(1,a):
        if a%i==0:
            suma_de_la_letra_a+=i

    for e in range(1,b):
        if b%e==0:
            suma_de_la_letra_b+=e

    return suma_de_la_letra_a==b and suma_de_la_letra_b==a