#Cálculo del dígito verificador de un rut

rut = input("Ingrese rut (sin puntos): ")

if (len(rut) == 8):
    aa = int(rut[7])
    ab = int(rut[6])
    ac = int(rut[5])
 
    ad = int(rut[4])
    ae = int(rut[3])
    af = int(rut[2])

    ag = int(rut[1])
    ah= int(rut[0])

    ba = (aa * 2)
    bb = (ab * 3)
    bc = (ac * 4)

    bd = (ad * 5)
    be = (ae * 6)
    bf = (af * 7)

    bg = (ag * 2)
    bh = (ah * 3)

    r = (ba + bb + bc + bd + be + bf + bg + bh)

    r1 = (r//11)
    r2 = r - (11 * r1)
    r_f = 11 - r2

    frase1 = "dv=" + str(r_f)

    if (r_f == 11):
        print("dv=0")

    elif (r_f == 10):
        print("dv=k")

    else:
        print(frase1)

elif (len(rut) == 7):
    ab = int(rut[6])
    ac = int(rut[5])
 
    ad = int(rut[4])
    ae = int(rut[3])
    af = int(rut[2])

    ag = int(rut[1])
    ah = int(rut[0])

    bb = (ab * 2)
    bc = (ac * 3)

    bd = (ad * 4)
    be = (ae * 5)
    bf = (af * 6)

    bg = (ag * 7)
    bh = (ah * 2)

    r = (bb + bc + bd + be + bf + bg + bh)
    
    r1 = (r//11)
    r2 = r - (11 * r1)
    r_f = 11 - r2

    frase1 = "dv=" + str(r_f)
    
    if (r_f == 11):
        print("dv=0")
    elif (r_f == 10):
        print("dv=k")
    else:
        print(frase1)