#datos.

ingresos = int(input("ingrese aqui sus Ingresos en pesos: $"))
año_nacimiento = int(input("ingrese aqui su año de nacimieno: "))
hijos = int(input("ingrese aqui su numero de hijos: "))
año_pertenecia = int(input("ingrese aqui sus Años de pertenencia en el banco: "))
estado_civil = (input("ingrese aqui su estado civil (S: soltero, C: casado): "))
campo_ciudad = (input("ingrese aqui si vive en el campo o en la ciudad (U: urbano, R: rural): "))

edad = (2020 - año_nacimiento)
#operaciones.

if año_pertenecia >= 10 and hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and hijos >= 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingresos >= 2500000 and estado_civil == "S" and campo_ciudad == "U":
    print("APROBADO")
elif ingresos >= 3500000 and año_pertenecia >= 5:
    print("APROBADO")
elif campo_ciudad == "R" and estado_civil == "C" and hijos <= 2:
    print("APROBADO")
else:
    print("Rechazado")