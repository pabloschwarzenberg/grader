#Aprobación de créditos

income = int(input("Ingresos liquidos del solicitante: "))
year_of_birth = int(input("Año nacimiento del solicitante: "))
number_of_child = int(input("Numero de hijos del solicitante: "))
years_in_bank = int(input("Años de pertenencia al banco: "))
marital_status = str(input("Estado civil del solicitante\nSoltero (S)\nCasado (C)\n: "))
marital_status = str(marital_status)
localidad = str(input("Residencia del solicitante\nCampo (U)\nCiudad (R)\n: "))
age = (int(2021)- year_of_birth)


if years_in_bank >= 10  and number_of_child >= 2:
    print("APROBADO")
elif marital_status == "C" and number_of_child >3 and 45 < age < 55:
    print("APROBADO")
elif income > 2500000 and marital_status == "s" and localidad == "r":
    print("APROBADO")
elif income > 3500000 and years_in_bank > 5:
    print("APROBADO")
elif localidad == "R" and marital_status == "C" and number_of_child < 2:
    print("APROBADO")
else:
    print("RECHAZADO")