#Aprobación de créditos
print("APROBACION DE CREDITOS")
INGRESO_PESOS= float(input("INGRESE SUS INGRESOS MONETARIOS EN PESOS: "))
A_N = int(input("INGRESE SU AÑO DE NACIMIENTO: "))
NRO_HIJOS = int(input("INGRESE LA CANTIDAD DE HIJOS (SI TIENE), DE CASO CONTRARIO INGRESE CERO(0): "))
A_P= int(input("INGRESE AÑOS DE PERTENECIA AL BANCO: "))
ESTADO_CIVIL=input("INGRESE SU ESTADO CIVIL, SI ES CASADO/A DIGITE (C), SI ES SOLTERO/A (S): ")
RESIDENCIA= input("INGRESE SU RESIDENCIA, SI VIVE EN ZONA URBANA DIGITE (U), SI VIVE EN ZONA RURAL (R): ")
EDAD = 2020-A_N
if INGRESO_PESOS<0:
    print("ERROR")
    print("EL MONTO INGRESADO ES INVALIDO")
    print("INGRESE VALORES POSITIVOS DE INGRESO MONETARIO POR FAVOR")
elif A_N<0:
    print("ERROR")
    print("EL AÑO INGRESADO ES INVALIDO")
    print("INGRESE VALORES POSITIVOS POR FAVOR")
elif NRO_HIJOS<0:
    print("ERROR")
    print("EL NUMERO DE HIJOS ES INVALIDO")
    print("INGRESE 0 SI NO TIENE HIJOS POR FAVOR")
    print("SI TIENE HIJOS INGRESE LA CANTIDAD EXACTA POSITIVA POR FAVOR")
elif A_P<0:
    print("ERROR")
    print("LOS AÑOS DE PERTENENCIA A LA EMPRESA INGRESADOS SON INVALIDOS")
    print("INGRESE VALORES POSITIVOS POR FAVOR")
elif ESTADO_CIVIL.isdigit():
    print("ERROR")
    print("EL ESTADO CIVIL INGRESADO ES INVALIDO")
    print("INGRESE (C) SI ES CASADO/A POR FAVOR")
    print("INGRESE (S) SI ES SOLTERO/A POR FAVOR")
elif RESIDENCIA.isdigit():
    print("ERROR")
    print("EL ESTADO CIVIL INGRESADO ES INVALIDO")
    print("INGRESE (U) SI VIVE EN ZONA URBANA POR FAVOR")
    print("INGRESE (R) SI VIVE EN ZONA RURAL POR FAVOR")
else:
    if A_P>10 and NRO_HIJOS>=2:
        print("APROBADO")
    elif NRO_HIJOS>3 and 55>EDAD>45:
        if ESTADO_CIVIL=="C" or ESTADO_CIVIL=="c":
            print("APROBADO")
        else:
            print("RECHAZADO")
    elif INGRESO_PESOS>2500000:
        if (ESTADO_CIVIL=="S" or ESTADO_CIVIL=="s") and (RESIDENCIA=="U" or RESIDENCIA=="u"):
            print("APROBADO")
        else:
            print("RECHAZADO")
    elif INGRESO_PESOS>3500000 and A_P>5:
        print("APROBADO")
    elif NRO_HIJOS<2:
        if (ESTADO_CIVIL=="C" or ESTADO_CIVIL=="c") and (RESIDENCIA=="R" or RESIDENCIA=="r"):
            print("APROBADO")
        else:
            print("RECHAZADO")
    else:
        print("RECHAZADO")      