#Aprobación de créditos
Ingresos=int(input("Ingresos:"))
Año_de_nacimiento=int(input("Año de nacimineto:"))
Numero_de_hijos=int(input("Numero de hijos:"))
Años_de_pertenecia_al_banco=int(input("Años de pertenencia al banco:"))
Estado_civil=input("Estado civil:")
Campo_o_ciudad=input("Campo o ciudad:")

if (Años_de_pertenecia_al_banco>10)and(Numero_de_hijos>=2):
    print("APROBADO")
else:
     print("NO APROBADO")
if (Estado_civil=="C")and(Numero_de_hijos>3)and(45<(2017-Año_de_nacimiento)<55):
    print("APROBADO")
else:
     print("NO APROBADO")
if (Ingresos>2500000)and(Estado_civil=="S")and(Campo_o_ciudad=="U"):
    print("APROBADO")
else:
     print("NO APROBADO")
if (Ingresos>3500000)and(Años_de_pertenecia_al_banco>5):
    print("APROBADO")
else:
        print("NO APROBADO")
if (Campo_o_ciudad=="R")and(Estado_civil=="C")and(Numero_de_hijos<2):
    print("APROBADO")
else:
        print("NO APROBADO")