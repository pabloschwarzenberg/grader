print("CALCULO DIGITO VERIFICADOR DEL RUT")
RUT = int(input("INGRESE SU RUT SIN GUION PUNTOS NI DIGITO VERIFICADOR: "))
if RUT<=0 or RUT>99999999:
    print("ERROR")
    print("EL RUT INGRESADO NO ES VALIDO")
elif RUT<999999:
    RUT = str(RUT)
    N1 = int(RUT[0]) * 7
    N2 = int(RUT[1]) * 6
    N3 = int(RUT[2]) * 5
    N4 = int(RUT[3]) * 4
    N5 = int(RUT[4]) * 3
    N6 = int(RUT[5]) * 2
    T = N1 + N2 + N3 + N4 + N5 + N6
    R = 11 - (T % 11)
    if R == 11:
        print("dv=0")
    elif R == 10:
        print("dv=k")
    else:
        print("dv=", R)
elif RUT<9999999:
    RUT = str(RUT)
    N1 = int(RUT[0]) * 2
    N2 = int(RUT[1]) * 7
    N3 = int(RUT[2]) * 6
    N4 = int(RUT[3]) * 5
    N5 = int(RUT[4]) * 4
    N6 = int(RUT[5]) * 3
    N7 = int(RUT[6]) * 2
    T = N1 + N2 + N3 + N4 + N5 + N6 + N7
    R = 11 - (T % 11)
    if R == 11:
        print("dv=0")
    elif R == 10:
        print("dv=k")
    else:
        print("dv=", R)
else:
    RUT=str(RUT)
    N1=int(RUT[0])*3
    N2=int(RUT[1])*2
    N3=int(RUT[2])*7
    N4=int(RUT[3])*6
    N5=int(RUT[4])*5
    N6=int(RUT[5])*4
    N7=int(RUT[6])*3
    N8=int(RUT[7])*2
    T=N1+N2+N3+N4+N5+N6+N7+N8
    R=11-(T%11)
    if R==11:
        print("dv=0")
    elif R==10:
        print("dv=k")
    else:
        print("dv=", R)