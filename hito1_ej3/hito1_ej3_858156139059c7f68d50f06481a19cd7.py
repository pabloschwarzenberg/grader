#aprobacion de credito
ingreso = int(input("INTRODUZCA SU INGRESO EN PESOS: "))
año_naci = int(input("INTRODUZCA SU AÑO DE NACIMIENTO: "))
num_hijos = int(input("INTRODUZCA EL TOTAL DE HIJOS QUE TIENE: "))
años_banco = int(input("INTRODUZCA EL TOTAL DE AÑOS QUE HA ESTADO EN EL BANCO:"))
estado_civil = str(input("¿SOLTERO O CASADO? s O c: "))
campo_ciudad = str(input("¿CAMPO O CIUDAD? u O r: "))
edad = 2022-año_naci
if años_banco > 10 and num_hijos >= 2:
    print("SU CREDITO SE HA APROBADO")
elif estado_civil == "c" and num_hijos > 3 and edad >=45 and edad <=55:
    print("SU CREDITO SE HA APROBADO")
elif ingreso > 2500000 and estado_civil == "s" and campo_ciudad == "u":
    print("SU CREDITO SE HA APROBADO")
elif ingreso > 3500000 and años_banco > 5:
    print("SU CREDITO SE HA APROBADO")
elif campo_ciudad == "r" and estado_civil == "c" and num_hijos < 2:
    print("SU CREDITO SE HA APROBADO")
else:
    print("SU CREDITO NO SE HA APROBADO")