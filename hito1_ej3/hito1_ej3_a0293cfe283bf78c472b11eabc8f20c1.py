ingreso = int(input("Ingreso en pesos: "))
año_de_nacimiento = int(input("Año de nacimiento: "))
numero_de_hijos = int(input("Numero de hijos: "))
años_de_pertenecia_al_banco = int(input("Años de pertenecia al banco: "))
estado_civil = input("Estado civil ,soltero(S) ,casado(C): ")
campo_ciudad = input("Si vive urbano(U) ,rural(R): ")
edad = 2020 - año_de_nacimiento
if años_de_pertenecia_al_banco > 10 and numero_de_hijos >= 2:
    print("APROBADO")
elif estado_civil.lower() == "c" and numero_de_hijos > 3 and 45 < edad < 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil.lower() == "s" and campo_ciudad.lower() == "u":
    print("APROBADO")
elif ingreso > 3500000 and años_de_pertenecia_al_banco > 5:
    print("APROBADO")
elif campo_ciudad.lower() == "r" and estado_civil.lower() == "c" and numero_de_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")