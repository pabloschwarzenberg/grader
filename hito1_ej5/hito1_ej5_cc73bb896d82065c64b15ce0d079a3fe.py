#Cálculo del dígito verificador de un rut
Rut = str(input("Ingrese un rut sin digito verificador:"))

if len(Rut) == 8:
    a = int(Rut[-1])
    b = int(Rut[-2])
    c = int(Rut[-3])
    d = int(Rut[-4])
    e = int(Rut[-5])
    f = int(Rut[-6])
    g = int(Rut[-7])
    h = int(Rut[-8])
    a2 = a * 2
    b2 = b * 3
    c2 = c * 4
    d2 = d * 5
    e2 = e * 6
    f2 = f * 7
    g2 = g * 2
    h2 = h * 3
    x = a2+b2+c2+d2+e2+f2+g2+h2
    Resto = x % 11
    Digito = 11 - Resto

    if Digito > 0 and Digito < 10 :
                print("dv =",Digito)

    if Digito == 11:
                print("dv = 0")

    if Digito == 10:
                print("dv = K")


if len(Rut) == 7:
    a = int(Rut[-1])
    b = int(Rut[-2])
    c = int(Rut[-3])
    d = int(Rut[-4])
    e = int(Rut[-5])
    f = int(Rut[-6])
    g = int(Rut[-7])
    a2 = a * 2
    b2 = b * 3
    c2 = c * 4
    d2 = d * 5
    e2 = e * 6
    f2 = f * 7
    g2 = g * 2
    x = a2+b2+c2+d2+e2+f2+g2
    Resto = x % 11
    Digito = 11 - Resto

    if Digito > 0 and Digito < 10 :
                print("dv =",Digito)

    if Digito == 11:
                print("dv = 0")

    if Digito == 10:
                print("dv = K")
