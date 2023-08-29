#Cálculo del dígito verificador de un rut
R = str(input("Ingrese rut sin digito verificador: "))

T = int(R)
if 1000000 <= T <= 9999999:
    b = int(R[6]) * 2
    c = int(R[5]) * 3
    d = int(R[4]) * 4
    e = int(R[3]) * 5
    o = int(R[2]) * 6
    g = int(R[1]) * 7
    h = int(R[0]) * 2
    p = (b + c + d + e + o + g + h)
    W = (p % 11)
    J = 11-W
    if J == 11:
        print("dv=", 0)
    elif J == 10:
        print("dv = K")
    else:
        print("dv =", J)

elif 10000000 <= T <= 99999999:
    a = int(R[7]) * 2
    k = int(R[6]) * 3
    z = int(R[5]) * 4
    x = int(R[4]) * 5
    v = int(R[3]) * 6
    n = int(R[2]) * 7
    m = int(R[1]) * 2
    u = int(R[0]) * 3
    G = (a + k + z + x + v + n + m + u)
    I = (G % 11)
    T = 11-I
    if T == 11:
        print("dv=", 0)
    elif T == 10:
        print("dv = K")
    else:
        print("dv =", T)


else:
    print("Rut no identificado")