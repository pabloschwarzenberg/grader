#Aprobación de créditos
ingreso= float(input("Ingreso (en pesos): "))
año= float(input("Año de nacimiento: "))
hijos= float(input("Número de hijos: "))
pertenencia= float(input("Años de pertenencia al banco: "))
estado= str(input("Estado civil (S: soltero , C, casado): ")).upper
vive= str(input("vive en: (U: urbano, R: rural): ")).upper
s=1
c=2
u=3
r=4
if pertenencia>10 or hijos>=2 and estado==2 or hijos>=3 or año<=1975 or año>=1965 and ingreso>2500000 or estado==1 and vive==3 and ingreso>3500000 or pertenencia>5 and vive==4 or estado==2 or hijos<=2:
    print("APROBADO")
else:
    print("RECHAZADO")