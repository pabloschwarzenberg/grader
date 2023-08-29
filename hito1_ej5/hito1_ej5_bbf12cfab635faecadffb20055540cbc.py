rut = str(input("Ingrese el RUT sin digito verificador ni puntos: "))
if len(rut) == 8:
    r1 = int(rut[-1])
    r2 = int(rut[-2])
    r3 = int(rut[-3])
    r4 = int(rut[-4])
    r5 = int(rut[-5])
    r6 = int(rut[-6])
    r7 = int(rut[-7])
    r8 = int(rut[-8])
    r1a = r1 * 2
    r2a = r2 * 3
    r3a = r3 * 4
    r4a = r4 * 5
    r5a = r5 * 6
    r6a = r6 * 7
    r7a = r7 * 2
    r8a = r8 * 3
    sumaf =(r1a + r2a + r3a + r4a + r5a + r6a + r7a + r8a)
    resto1 = sumaf % 11
    Verificador = 11 - resto1
    if 0 < Verificador < 10:
        print("dv =", Verificador)
    else:
        if Verificador == 11:
            print("dv=0")
        else:
            if Verificador == 10:
                print("dv=k")
if len(rut)== 7:
    r1 = int(rut[-1])
    r2 = int(rut[-2])
    r3 = int(rut[-3])
    r4 = int(rut[-4])
    r5 = int(rut[-5])
    r6 = int(rut[-6])
    r7 = int(rut[-7])
    r1a = r1 * 2
    r2a = r2 * 3
    r3a = r3 * 4
    r4a = r4 * 5
    r5a = r5 * 6
    r6a = r6 * 7
    r7a = r7 * 2
    sumaf2 = (r1a + r2a + r3a + r4a + r5a + r6a + r7a)
    Verificador1 = 11 - (sumaf2 % 11)
    if 0< Verificador1 < 10:
        print("dv =", Verificador1)
    else:
        if Verificador1 == 11:
            print("dv = 0")
        else:
            if Verificador1 == 10:
                print("dv=k")