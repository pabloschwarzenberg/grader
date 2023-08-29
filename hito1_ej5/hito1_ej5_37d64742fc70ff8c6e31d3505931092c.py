#Cálculo del dígito verificador de un rut
print("Calcular el numero verificador.")
rut = str(input("Ingrese el rut sin puntos: "))
if len(rut) == 7 :
    a = int(rut[-1])
    b = int(rut[-2])
    c = int(rut[-3])
    d = int(rut[-4])
    e = int(rut[-5])
    f = int(rut[-6])
    g = int(rut[-7])
    ax = a * 2
    bx = b * 3
    cx = c * 4
    dx = d * 5
    ex = e * 6
    fx = f * 7
    gx = g * 2
    suma = (ax + bx + cx + dx + ex + fx + gx)
    modulo = suma // 11
    div = suma - (11 * modulo)
    dv = 11 - div
    dv = str(dv)

    if str(dv) == "11":
        print("dv = 0")
    else:
        if str(dv) == "10":
            print("dv = k")
        else:
            print("dv = " + dv)
if len(rut) == 8 :
    a = int(rut[-1])
    b = int(rut[-2])
    c = int(rut[-3])
    d = int(rut[-4])
    e = int(rut[-5])
    f = int(rut[-6])
    g = int(rut[-7])
    h = int(rut[-8])
    ax = a * 2
    bx = b * 3
    cx = c * 4
    dx = d * 5
    ex = e * 6
    fx = f * 7
    gx = g * 2
    hx = h * 3
    suma = (ax + bx + cx + dx + ex + fx + gx + hx)
    modulo = suma // 11
    div = suma - (11 * modulo)
    dv = 11 - div
    dv = str(dv)

    if str(dv) == "11":
        print("dv = 0")
    else:
        if str(dv) == "10":
            print("dv = k")
        else:
            print("dv = " + dv)