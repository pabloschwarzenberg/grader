#Cálculo del dígito verificador de un rut
rut = input("Ingrese RUT (Sin puntos y sin en numero verificador): ")

if (len(rut) == 8):
    a1 = int(rut[7])
    a2 = int(rut[6])
    a3 = int(rut[5])
 
    a4 = int(rut[4])
    a5 = int(rut[3])
    a6 = int(rut[2])

    a7 = int(rut[1])
    a8 = int(rut[0])

    b1 = (a1 * 2)
    b2 = (a2 * 3)
    b3 = (a3 * 4)

    b4 = (a4 * 5)
    b5 = (a5 * 6)
    b6 = (a6 * 7)

    b7 = (a7 * 2)
    b8 = (a8 * 3)

    r = (b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8)

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
    a2 = int(rut[6])
    a3 = int(rut[5])
 
    a4 = int(rut[4])
    a5 = int(rut[3])
    a6 = int(rut[2])

    a7 = int(rut[1])
    a8 = int(rut[0])

    b2 = (a2 * 2)
    b3 = (a3 * 3)

    b4 = (a4 * 4)
    b5 = (a5 * 5)
    b6 = (a6 * 6)

    b7 = (a7 * 7)
    b8 = (a8 * 2)

    r = (b2 + b3 + b4 + b5 + b6 + b7 + b8)

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