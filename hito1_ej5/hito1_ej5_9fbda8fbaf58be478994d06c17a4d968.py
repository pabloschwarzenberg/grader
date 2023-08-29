rut = str(input("Ingrese rut sin puntos ni digito verificador: "))
if len(rut) == 7:
    rut = "0" + rut
    
N1I = rut[0:1]
N1F = int(N1I)

N2I = rut[1:2]
N2F = int(N2I)

N3I = rut[2:3]
N3F = int(N3I)

N4I = rut[3:4]
N4F = int(N4I)

N5I = rut[4:5]
N5F = int(N5I)

N6I = rut[5:6]
N6F = int(N6I)

N7I = rut[6:7]
N7F = int(N7I)

N8I = rut[7:8]
N8F = int(N8I)


n8 = N8F * 2
n7 = N7F * 3
n6 = N6F * 4
n5 = N5F * 5
n4 = N4F * 6
n3 = N3F * 7
n2 = N2F * 2
n1 = N1F * 3

suma_total = n8 + n7 + n6 + n5 + n4 + n3 + n2 + n1
division_entera = suma_total // 11
resto = suma_total -(11 * division_entera)
dvf = 11 - resto

if dvf == 11:
    print("dv = 0")

elif dvf == 10:
    print("dv = K")

else:
    print("dv =",dvf)
