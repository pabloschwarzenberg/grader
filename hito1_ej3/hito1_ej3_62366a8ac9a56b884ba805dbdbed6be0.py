#Aprobación de créditos
# Entrada

pesos = input("Ingresos ")
years = input("Año de nacimento ")
kids = input("Numero de hijos ")
banky = input("Años de pertenecia al banco ")
EC = input("Estado civil ('S': soltero,'C',casado) ")
Viv = input("Si vive en el campo o la ciudad ('U': urbano, 'R': rural) ")

# Procesamiento
if float(banky) > 10 and int(kids) >= 2:
    print("APROBADO.")
elif EC == str("C") and int(kids) > 3 and 1976 >= int(years) >= 1966:
    print("APROBADO.")
elif int(pesos) > 2500000 and EC == str("S") and Viv == str("U"):
    print("APROBADO.")
elif int(pesos) > 3500000 and float(banky) > 5:
    print("APROBADO.")
elif Viv == str("R") and EC == str("C") and int(kids) < 2:
    print("APROBADO.")
else:
    print("RECHAZADO.")