#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su rut: "))
if rut <= 99999999 and rut >= 1000000:
    q = rut // 10000000
    s = rut % 10000000
    w = s // 1000000
    s = s % 1000000
    e = s // 100000
    s = s % 100000
    r = s // 10000
    s = s % 10000
    t = s // 1000
    s = s % 1000
    y = s // 100
    s = s % 100
    u = s // 10
    s = s % 10
    operacion = (q*3)+(w*2)+(e*7)+(r*6)+(t*5)+(y*4)+(u*3)+(s*2)
    operacion2 = operacion // 11
    operacion3 = operacion-(11*operacion2)
    operacion4 = 11 - operacion3

    if operacion4 == 11:
        print("dv=0")
    elif operacion4 == 10:
        print("dv=k")
    else:
        print("dv=", operacion4)      