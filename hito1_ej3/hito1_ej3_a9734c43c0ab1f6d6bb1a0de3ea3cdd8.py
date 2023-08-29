#Aprobación de créditos
Ingreso=int(input("Ingreso:"))
year_nacimiento=int(input("Ingrese fecha de nacimiento:"))
Numero_de_hijos=int(input("Ingrese numero de hijos:"))
Tiempo_de_pertenencia=int(input("Ingrese tiempo de pertenencia:"))
Estado_civil=str(input("Igrese S: soltero o C: casado:"))
Si_vive_en_campo_o_cuidad=str(input("ingrese U: urbano o R: rural:"))
if Tiempo_de_pertenencia>10 and Numero_de_hijos>=2:
    print("APROBADO")
elif Estado_civil=="C" and Numero_de_hijos>3 and 1969<year_nacimiento<1981:
    print("APROBADO")
elif Ingreso>2500000 and Estado_civil=="S" and Si_vive_en_campo_o_cuidad=="U":
    print("APROBADO")
elif Ingreso>3500000 and Tiempo_de_pertenencia>5:
    print("APROBADO")
elif Si_vive_en_campo_o_cuidad=="R" and Estado_civil=="C" and Numero_de_hijos<2:
    print("APROBADO")     