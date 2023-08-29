x = str(input("ingrece su rut:"))
T =int(x)
if 1000000 <= T <=9999999:
    a = int(x[6]) * 2
    b = int(x[5]) * 3
    c = int(x[4]) * 4
    d = int(x[3]) * 5
    e = int(x[2]) * 6
    f = int(x[1]) * 7
    g = int(x[0]) * 2
    suma = (a + b + c + d + e + f +g)

    sumat = (suma % 11)
    var = 11-sumat
    if var == 11:
       print("dv=0")
    elif var == 10:
       print("dv=K")
    else: 
      print("dv=", var)
elif 10000000 <= T <=99999999:
    H= int(x[7]) * 2
    I = int(x[6]) * 3
    J = int(x[5]) * 4
    K = int(x[4]) * 5
    L = int(x[3]) * 6
    M = int(x[2]) * 7
    N = int(x[1]) * 2
    Ñ = int(x[0]) * 3
    suma = (H + I + J + K + L + M + N + Ñ)
    i = ( suma % 11)
    t = 11-i
    if t == 11:
        print("dv=0")
    elif t == 10:
        print("dv=K")
    else:
        print("dv =", t)


else:
    print("rut no identificado")
        
    