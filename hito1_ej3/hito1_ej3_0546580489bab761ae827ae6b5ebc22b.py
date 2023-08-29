#Aprobación de créditos

ingreso = int(input("Digite su ingreso: "))
adn = int(input("Ingrese anio de nacimiento: "))
ndh = int(input("Ingrese su numero de hijos: "))
apb = int(input("Ingrese los anios de pertenencia al banco: "))
ec = input("Ingrese Estado civil (S = SOLTERO) (C = CASADO)")
vnda = input("Ingrese vivienda (U = urbano) (R = rural)")

if apb > 10 and ndh >= 2:
    print("APROBADO")
elif ec == 'C' and ndh > 3 and 1976 < adn < 1966:
    print("APROBADO")
elif ingreso > 2500000 and ec == 'S' and vnda == 'U':
    print("APROBADO")
elif ingreso > 3500000 and apb > 5:
    print("APROBADO")
elif vnda == 'R' and ec == 'C' and ndh < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      