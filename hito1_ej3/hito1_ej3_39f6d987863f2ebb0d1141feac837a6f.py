#Aprobación de créditos
ingreso= int(input("Ingreso(en pesos): "))
nacimiento= int(input("Año de nacimiento: "))
hijos= int(input("Número de hijos: "))
años_banco= int(input("Años de pertenencia al banco: "))
estado= input("Estado civil (S: soltero, C: casado)")
campo_ciudad= input("Vive en campo o ciudad (U: urbano, R: rural)")

if años_banco > 10 and hijos >= 2:
    print("APROBADO")
elif estado=="C" and hijos>3 and (2021-nacimiento)>45 and (2021-nacimiento)<55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and campo_ciudad=="U":
    print("APROBADO")
elif ingreso>3500000 and años_banco>5:
    print("APROBADO")
elif campo_ciudad=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")