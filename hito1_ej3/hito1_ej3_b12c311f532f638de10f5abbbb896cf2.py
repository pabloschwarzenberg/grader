#Aprobación de créditos
ingresos= int(input("ingresos: "))
ano_n= int(input("Año de nacimiento: "))
hijos= int(input("Numero de hijos: "))
anos_pert= int(input("Cuantos años lleva con el banco: "))
est_civil= input("Estado civil(s:soltero, C:casado): ")
campo_ciudad= input("Es de campo o ciudad(U:urbano, R:rural): ")

if(anos_pert>10 and hijos>=2 or est_civil=="C" and hijos>3 and 1966<=ano_n<=1976 or ingresos>2500000 and est_civil=="S" and campo_ciudad=="U" or ingresos>3500000 and anos_pert>=5 or campo_ciudad=="R" and est_civil=="C" and hijos<2):
    print("APROVADO")
else:
    print("RECHAZADO")