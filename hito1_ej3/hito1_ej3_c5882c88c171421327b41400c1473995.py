#Aprobación de créditos
ingreso=input("ingreso en pesos: ")
anno_nacimiento=input("año de nacimiento: ")
numero_hijos=input("numero de hijos: ")
annos_pertenencia=input("años de pertenencia al banco: ")
estado_civil=input("estado civil: ")
campo_o_ciudad=input("vive en espacio urbano, o rural?: ")

if int(annos_pertenencia) > 10 and int(numero_hijos) >= 2:
    print("APROBADO")
elif estado_civil == "casado" and int(numero_hijos) > 3 and int(anno_nacimiento) >= 1966 or int(anno_nacimiento) <= 1976:
    print("APROBADO")
elif int(ingreso) > 2500000 and estado_civil == "soltero" and campo_o_ciudad =="ciudad":
    print("APROBADO")
elif int(ingreso)>3500000 and int(annos_pertenencia)> 5:
    print("APROBADO")
elif campo_o_ciudad=="campo" and estado_civil=="casado" and int(numero_hijos)<2:
    print("APROBADO")
else:
    print("RECHAZADO")