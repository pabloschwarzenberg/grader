#Aprobación de créditos
a=float(input("Ingreso: "))
b=float(input("Año de nacimiento: "))
c=float(input("Número de hijos: "))
d=float(input("Años de pertenencia al banco: "))
e=(input("Estado civil (S: soltero, C, casado): "))
f=(input("Vives en campo o cuidad (U: urbano, R: rural): "))
if d>10 and c>=2 :
    print("APROBADO")
elif e=="C" and c>3 and ((2016-b)>=45 and (2016-b)<=55) :
    print("APROBADO")
elif e=="S" and a>2500000 and f=="U" :
    print("APROBADO")
elif a>3500000 and d>5 :
    print("APROBADO")
elif f=="R" and e=="C" and c<2 :
    print("APROBADO")
else :
    print("RECHAZADO") 
