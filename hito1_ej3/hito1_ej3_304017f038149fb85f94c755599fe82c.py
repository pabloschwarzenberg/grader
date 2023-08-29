ingresos= int(input("ingrese el total de ingresos"))
a_nacimiento= int(input("ingrese el año de nacimiento"))
num_hijos= int(input("ingrese el número de hijos"))
a_pert_banc= int(input("ingrese los años de pertenencia al banco"))
edad= 2022-a_nacimiento
estado_civil= input("ingrese su estado civil, si está casado c, si está soltero s")
campo_ciudad= input("ingrese u si vive en una zona urbana, o r si vive en una zona rural")
if estado_civil == "c" and num_hijos > 3 and 45 > edad > 55 and a_pert_banc == a_pert_banc and campo_ciudad == campo_ciudad and ingresos== ingresos and a_nacimiento == a_nacimiento and :
    print("APROBADO")
elif ingresos > 2500000 and estado_civil == "s" and campo_ciudad == "u":
    print("APROBADO")
elif ingresos > 3500000 and a_pert_banc > 5:
    print("APROBADO")
elif campo_ciudad == "r" and estado_civil == "c" and num_hijos < 2:
    print("APROBADO")
elif a_pert_banc > 10 and num_hijos >= 2:
    print("APROBADO")
else:
    print("RECHAZADO")