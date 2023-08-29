#Cálculo del dígito verificador de un rut
RUT = str(input("Ingrese el rut sin puntos: "))
if len(RUT) == 7:
    n1 = int(RUT[-1])
    n2 = int(RUT[-2])
    n3 = int(RUT[-3])
    n4 = int(RUT[-4])
    n5 = int(RUT[-5])
    n6 = int(RUT[-6])
    n7 = int(RUT[-7])
    N1 = n1 * 2
    N2 = n2 * 3
    N3 = n3 * 4
    N4 = n4 * 5
    N5 = n5 * 6
    N6 = n6 * 7
    N7 = n7 * 2
    Suma = N1 + N2 + N3 + N4 + N5 + N6 + N7
    ParteEntera = Suma // 11
    RestoParteEntera = Suma - (11 * ParteEntera)
    DV = 11 - RestoParteEntera
    if DV < 10 and DV > 0:
        print("dv =",DV)
    elif DV == 10:
        print("dv = k")
    elif DV == 11:
        print("dv = 0")
else:
    if len(RUT) == 8:
        n1 = int(RUT[-1])
        n2 = int(RUT[-2])
        n3 = int(RUT[-3])
        n4 = int(RUT[-4])
        n5 = int(RUT[-5])
        n6 = int(RUT[-6])
        n7 = int(RUT[-7])
        n8 = int(RUT[-8])
        N1 = n1 * 2
        N2 = n2 * 3
        N3 = n3 * 4
        N4 = n4 * 5
        N5 = n5 * 6
        N6 = n6 * 7
        N7 = n7 * 2
        N8 = n8 * 3
        Suma = N1 + N2 + N3 + N4 + N5 + N6 + N7 + N8
        ParteEntera = Suma // 11
        RestoParteEntera = Suma - (11 * ParteEntera)
        DV = 11 - RestoParteEntera
        if DV < 10 and DV > 0:
            print("dv =",DV)
        if DV == 10:
            print("dv = K")
        if DV == 11:
            print("dv = 0")