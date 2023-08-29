ingreso = int(input("Ingreso: "))
a_nacimiento = int(input("Año de nacimiento: "))
n_hijos = int(input("Número de hijos: "))
a_pertenencia_banco = int(input("Años de pertenencia al banco: "))
estado_civil = input("Estado civil (S: Soltero, C: Casado): ")
campo_o_ciudad = input("Donde vive (U: Urbano, R: Rural): ")

if a_pertenencia_banco > 10 and n_hijos >= 2:
    print("APROBADO")
elif estado_civil == 'C' and n_hijos > 3 and 45 <= a_nacimiento <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == 'S' and campo_o_ciudad == 'U':
    print("APROBADO")
elif ingreso > 3500000 and a_pertenencia_banco > 5:
    print("APROBADO")
elif campo_o_ciudad == 'R' and estado_civil == 'C' and n_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")