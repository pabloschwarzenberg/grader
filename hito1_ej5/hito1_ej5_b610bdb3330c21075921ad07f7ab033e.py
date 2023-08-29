#Cálculo del dígito verificador de un rut
      # Inputs ETC
 #RUT
rut_sin_DF = input("Ingrese un numero rut sin numero verificador:")

# Algoritmo
serie_1 = int((rut_sin_DF[-1])) * 2
serie_2 = int((rut_sin_DF[-2])) * 3
serie_3 = int((rut_sin_DF[-3])) * 4
serie_4 = int((rut_sin_DF[-4])) * 5
serie_5 = int((rut_sin_DF[-5])) * 6
serie_6 = int((rut_sin_DF[-6])) * 7
serie_7 = int((rut_sin_DF[-7])) * 2
serie_8 = int((rut_sin_DF[-8])) * 3
# Suma de series
suma_total = serie_1 + serie_2 + serie_3 + serie_4 + serie_5 + serie_6 + serie_7 + serie_8

# Restos
resto_1 = (suma_total)//11

resto_2 = (suma_total)-(11*(resto_1))

#DV

dv = 11-resto_2
if dv == 11:
    print("dv = 0",)
if dv == 10:
    print("dv = K")
if dv < 10:
    print("dv=",dv)

