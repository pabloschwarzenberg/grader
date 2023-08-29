#Aprobación de créditos
ingreso=input("Ingrese su ingrso en pesos: ")
año_nacimiento=input("Ingrese su fecha de nacimiento: ")
numero_hijos=input("Ingrese numero de hijos: ")
año_pertenencia=input("Ingrese la cantidad de años que lleva perteneciendo a este bamco: ")
estado_civil=input("Ingrese su estado civil: ")
vive=input("Ingrese si vive en campo o ciudad: ")

if (((int(año_pertenencia))>10 and (int(numero_hijos))>=2) or ((45<(2017-int(año_nacimiento)<55) and (int(numero_hijos)>3) and (estado_civil=="c",True)) or ((int(ingreso)>2500000) and (estado_civil=="s", True) and (vive=="u", True)) or ((int(ingreso)>3500000) and (int(año_pertenencia)>5)) or ((vive=="r", True) and (estado_civil=="c", True) and (int(numero_hijos)<2)))):
    print("APROBADO")
else:
        print("REPROBADO")

