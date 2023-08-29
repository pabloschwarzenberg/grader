#Aprobación de créditos
Ingreso = int(input("Ingreso: "))
BD = int(input("Año de nacimiento: "))
NH = int(input("Numero de hijos: "))
apb = int(input("Años de pertenencia al banco: "))
print("'S':soltero")
print("'C':casado")
EC = str(input("Estado Civil: "))
print("'U':urbano")
print("'R':rural")
EC = str(input("Estado Civil: "))
X = 2020 - BD
if (apb > 10 and NH >= 2):
    print("APROBADO")
elif (EC == 'C' and NH > 3 and X > 45 or X < 55):
    print("APROBADO")
elif (Ingreso > 2500000 and apb == 'S' and EC == 'U'):
    print("APROBADO")
elif (Ingreso > 3500000 and apb > 5):
    print("APROBADO")
elif (EC == 'R' and apb == 'C' and NH < 2):
    print("APROBADO")
else:
    print("RECHAZADO")

      