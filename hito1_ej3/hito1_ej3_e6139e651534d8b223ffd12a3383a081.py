I=int(input("Ingreso (en pesos):"))
AN= int(input("Año de nacimiento:"))
NH= int(input("Número de hijos:"))
APB= int(input("Años de pertenencia al banco:"))
EC= input("Estado civil, (S): soltero, (C), casado:")
V= input("Si vive en campo o cuidad (U= urbano, R= rural):")
if (APB>10) and (NH >=2) or (EC=="C")and (NH >3) and (45<=(2022-AN)<=55) or (I>2500000) and (EC=="S") and (V=="U") or (I>3500000) and (APB>5)or(V=="R") and (EC=="C") and (NH<2):
    print ("APROBADO")
else:
    print ("RECHAZADO")