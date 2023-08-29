rut = str(input("Ingrese rut sin digito verificador"))

T = int(rut)
if 1000000 <= T <= 9999999:
    n1 = int(rut[6]) * 2
    n2 = int(rut[5]) * 3
    n3 = int(rut[4]) * 4
    n4 = int(rut[3]) * 5
    n5 = int(rut[2]) * 6
    n6 = int(rut[1]) * 7
    n7 = int(rut[0]) * 2
    suma_7_numeros = n1+n2+n3+n4+n5+n6+n7
    division_7_numeros = suma_7_numeros % 11
    resta_7_numeros = 11 - division_7_numeros

    if resta_7_numeros == 11:
        print("El dv= 0 ")
    elif resta_7_numeros == 10:
        print("El dv= k ")
    else:
        print("El dv= ",resta_7_numeros)
        
elif 10000000 <= T <= 99999999:
    N1 = int(rut[7]) * 2
    N2 = int(rut[6]) * 3
    N3 = int(rut[5]) * 4
    N4 = int(rut[4]) * 5
    N5 = int(rut[3]) * 6
    N6 = int(rut[2]) * 7
    N7 = int(rut[1]) * 2
    N8 = int(rut[0]) * 3
    suma_8_numeros = N1 + N2 + N3 + N4 + N5 + N6 + N7 + N8
    division_8_numeros = suma_8_numeros % 11
    resta_8_numeros = 11 - division_8_numeros

    if resta_8_numeros == 11:
        print("El dv= 0 ")
    elif resta_8_numeros == 10:
        print("El dv= k ")
    else:
        print("El dv= ", resta_8_numeros)
        
else:
    print("rut invalido")