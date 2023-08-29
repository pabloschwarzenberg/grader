int_ingreso= int(input("Ingrese su ingreso: "))
int_anno_nacimiento = int(input("Ingrese su año de nacimiento: "))
int_numero_hijos = int(input("Ingrese su número de hijos: "))
int_annos_pertenencia = int(input("Ingrese sus años de pertenencia al banco: "))
str_estado_civil= str(input("Ingrese su estado civil (S: soltero, C: casado): "))
str_ciudad= str(input("Ingrese si vive en campo o cuidad (U: urbano, R: rural): "))
if (int_annos_pertenencia > 10 and int_numero_hijos >= 2):
    print("APROBADO")
elif (str_estado_civil == "C" and int_numero_hijos > 3 and int_anno_nacimiento >= 45 and int_anno_nacimiento <= 55):
    print("APROBADO")
elif (int_ingreso > 2500000 and str_estado_civil == "S" and str_ciudad == "U"):
    print("APROBADO")
elif (int_ingreso > 3500000 and int_annos_pertenencia > 5):
    print("APROBADO")
elif (str_ciudad == "R" and str_estado_civil == "C" and int_numero_hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")