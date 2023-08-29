#Aprobación de créditos
ingresos = int(input("ingrsos mensuales: $"))
ano = int(input("Ingrese su año de nacimiento:",))
hijos = int(input("¿Cantidad de hijos?:",))
banco = int(input("¿Cantidad de años en el banco?:",))
estado = input("¿Estado civil?(C para casado, S para soltero) :",)
lugar = input("¿Lugar de residencia?(U=urbano, R=rural) :")
if (banco > 10) and (hijos >= 2):
    print("APROBADO")
elif (estado=="C") and (hijos > 3) and (1965 < ano < 1975):
    print("APROBADO")
elif (ingresos > 2500000) and (estado=="S") and (lugar=="U"):
    print("APROBADO")
elif (ingresos > 3500000) and (banco > 5):
    print("APROBADO")
elif (lugar=="R") and (estado=="C") and (hijos < 2):
    print("APROBADO")
else :
    print("RECHAZADO")