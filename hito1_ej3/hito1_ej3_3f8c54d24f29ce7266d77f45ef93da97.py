#Aprobación de créditos
ingreso = int(input("ingrese el numero de ingreso en pesos: "))
Año_de_nacimiento = int(input("ingrese el año de nacimiento: "))
Numero_de_hijos = int(input("ingrese el numero de hijos que tiene: "))
Años_de_pertenencia_al_banco = int(input("ingrese Años de pertenencia al banco"))
Estado_civil = str(input("ingrese estado civil (soltero = S, casado = C): "))
Si_vive_en_campo_o_cuidad = str(input("Ingrese zona recidencial (urbano = U, rural = R): "))

if Años_de_pertenencia_al_banco > 10 and Numero_de_hijos >= 2:
    print("APROBADO")

elif Estado_civil == "C" and Numero_de_hijos > 3 and 2023 - Año_de_nacimiento > 45 and 2023 - Año_de_nacimiento < 55:
    print("APROBADO")

elif ingreso > 2500000 and Estado_civil == "S" and Si_vive_en_campo_o_cuidad == "U":
    print("APROBADO")

elif ingreso >3500000 and Años_de_pertenencia_al_banco > 5:
    print("APROBADO")

elif Si_vive_en_campo_o_cuidad == "R" and Numero_de_hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")