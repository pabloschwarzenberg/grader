rut = (input("Ingrese rut: "))
if len(rut) == 7:
    a1 = int(rut[0])
    a2 = int(rut[1])
    a3 = int(rut[2])
    a4 = int(rut[3])
    a5 = int(rut[4])
    a6 = int(rut[5])
    a7 = int(rut[6])
    suma = (a7*2)+(a6*3)+(a5*4)+(a4*5)+(a3*6)+(a2*7)+(a1*2)
else:
    a1 = int(rut[0])
    a2 = int(rut[1])
    a3 = int(rut[2])
    a4 = int(rut[3])
    a5 = int(rut[4])
    a6 = int(rut[5])
    a7 = int(rut[6])
    a8 = int(rut[7])
    suma = (a8 * 2) + (a7 * 3) + (a6 * 4) + (a5 * 5) + (a4 * 6) + (a3 * 7) + (a2 * 2) + (a1 * 3)

resto = suma//11
multi = resto*11
sustraccion = suma - multi
code = 11 - sustraccion
if code == 11:
    print("dv=0")
elif code == 10:
    print("dv=k")
else:
    print("dv=",code)