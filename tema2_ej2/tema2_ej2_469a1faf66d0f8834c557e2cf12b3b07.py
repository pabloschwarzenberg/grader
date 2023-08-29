#completa el codigo de la funcion 
def numeros_amigos(a,b):
    suma_a = 0
    suma_b = 0
    vdd = False
    for i in range(1,a):
        if ((a % i) == 0):
            suma_a = i + suma_a
    for j in range(1,b):
        if ((b % j) == 0):
            suma_b = j + suma_b  
    if (suma_a==b and suma_b==a):
        vdd = True
    else:
        vdd = False
    return vdd
