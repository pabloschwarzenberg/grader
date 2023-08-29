#Aprobación de créditos
ingreso=int(input("Ingreso mensual: "))
año_de_nacimiento=int(input("Ingrese año de nacimiento: "))
numero_de_hijos=int(input("Ingrese numero de hijos: "))
años_en_el_banco=int(input("Ingresar cantidad de años que lleva en el banco: "))
estado_civil=input("Ingresar S si esta soltero o C si esta casado: ")
campo_ciudad=input("Ingresar U si vive en ciudad o R si vive en el campo: ")
año_actual=2022
edad=año_actual-año_de_nacimiento

if años_en_el_banco>10 and numero_de_hijos>=2:
    print("CREDITO APROBADO")
elif estado_civil=="C" and numero_de_hijos>3 and (edad>45 and edad<55):
    print("CREDITO APROBADO")
elif ingreso>2500000 and estado_civil=="S" and campo_ciudad=="U":
    print("CREDITO APROBADO")
elif ingreso>3500000 and años_en_el_banco>5:
    print("CREDITO APROBADO")
elif campo_ciudad=="R" and estado_civil=="C" and numero_de_hijos<2:
    print("CREDITO APROBADO")
else:
    print("CREDITO RECHAZADO")