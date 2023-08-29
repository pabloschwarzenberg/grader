#Aprobación de créditos
print("Aprovacion de credito")
ingreso = float(input("Ingrese su ingreso en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese cuantos hijos tiene: "))
años_de_pertenencia = int(input("Ingrese cuantos años ha pertenecido al banco: "))
estado_civil = input("Ingrese su estado civil donde s es soltero y c es casado: ")
vivienda = input("ingrese su residencia donde u es urbano y r es rural: ")

if años_de_pertenencia > 10 and hijos >= 2 and ingreso != 0 and nacimiento != 0 and estado_civil == 's' or 'c' and vivienda == 'u' or 'r':
    print("APROBADO")
elif estado_civil == 'c' and hijos > 3 and 45 <= (2023 - nacimiento) <= 55 and ingreso != 0 and años_de_pertenencia != 0 and vivienda == 'u' or 'r':
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == 's' and vivienda == 'u' and nacimiento != 0 and hijos >= 0 and años_de_pertenencia != 0:
    print("APROBADO")
elif ingreso > 3500000 and años_de_pertenencia > 5 and nacimiento != 0 and hijos >= 0 and estado_civil == 's' or 'c' and vivienda == 'u' or 'r':
    print("APROBADO")
elif vivienda == 'r' and estado_civil == 'c' and hijos < 2 and ingreso != 0 and nacimiento != 0 and años_de_pertenencia != 0:
    print("APROBADO")
else:
    print("RECHAZADO")