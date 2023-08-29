#Cálculo del dígito verificador de un rut
rut = str(input("Ingrese rut sin digito verificador"))

A = int(rut)
if 1000000 <= A <= 9999999:
    n1 = int(rut[6]) * 2
    n2 = int(rut[5]) * 3
    n3 = int(rut[4]) * 4
    n4 = int(rut[3]) * 5
    n5 = int(rut[2]) * 6
    n6 = int(rut[1]) * 7
    n7 = int(rut[0]) * 2
    suma1 = n1 + n2 + n3 + n4 + n5 + n6 + n7
    division = suma1 % 11
    resta1 = 11 - division

    if resta1 == 11:
        print("El dv= 0 ")
    elif resta1 == 10:
        print("El dv= k ")
    else:
        print("El dv= ", resta1)

elif 10000000 <= A <= 99999999:
    N8 = int(rut[7]) * 2
    N9 = int(rut[6]) * 3
    N10 = int(rut[5]) * 4
    N11 = int(rut[4]) * 5
    N12 = int(rut[3]) * 6
    N13 = int(rut[2]) * 7
    N14 = int(rut[1]) * 2
    N15 = int(rut[0]) * 3
    suma2 = (N8 + N9 + N10 + N11 + N12 + N13 + N14 + N15)
    division2 = suma2 % 11
    resta2 = 11 - division2

    if resta2 == 11:
        print("El dv= 0 ")
    elif resta2 == 10:
        print("El dv= k ")
    else:
        print("El dv= ", resta2)

else:
    print("rut invalido")