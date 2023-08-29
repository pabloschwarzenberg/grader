#Aprobación de créditos
#Entrada
#Entrada
ingreso = int(input("Entrege su ingreso en pesos: "))
ano_de_nacimiento = int(input("Ingrese su año de nacimiento: "))
numero_de_hijos = int(input("Ingrese su numero de hijos: "))
ano_de_pertenencia_al_banco = int(input("Ingrese ano de pertenencia: "))
estado_civil = input("Ingrese su estado civil ('S' = soltero , 'C' = casado):")
ubicacion = input("Ingrese su ubicacion ('U' = urbano , 'R' = rural):")



if ano_de_pertenencia_al_banco > 10 and numero_de_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and numero_de_hijos > 3 and (1975 >= ano_de_nacimiento >= 1965):
        print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == r:
        print("APROBADO")
elif ingreso > 3500000 and ano_de_pertenencia_al_banco > 5:
        print("APROBADO")
elif ubicacion == "R" and estado_civil == "C" and numero_de_hijos < 2:
        print("APROBADO")
else:
    print("RECHAZO")