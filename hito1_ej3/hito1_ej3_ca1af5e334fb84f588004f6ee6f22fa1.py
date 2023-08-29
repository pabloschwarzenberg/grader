i= float(input("Ingreso (en pesos): "))
a= int(input("Año de nacimiento: "))
nh= int(input("Número de hijos: "))
ap= int(input("Años de pertenencia al banco: "))
ec=input("Estado civil (S:soltero, C:Casado): ")
cc=input("Vive en campo o ciudad (U:urbano, R: rural): ")
if ap>10 and nh>=2:
    print("APROBADO")
elif ec=="C" and nh>3 and 1970<=a>=1980:
    print("APROBADO")
elif i>=250000 and ec=="S" and cc=="U":
    print("APROBADO")
elif i>=350000 and ap>=5:
    print("APROBADO")
elif cc=="R" and ec=="C" and nh<=2:
    print ("APROBADO")
else:
    print ("RECHAZADO")