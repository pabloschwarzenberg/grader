#Aprobación de créditos
i=int(input("Ingreso (en pesos):"))
n=int(input("Año de nacimiento:"))
h=int(input("Número de hijos:"))
a=int(input("Años de pertenencia al banco:"))
e=str(input("Estado civil (S: soltero, C: casado):"))
v=str(input("Vive en campo o cuidad (U: urbano, R: rural):"))
if a>10 and h>=2:
    print("APROBADO")
elif e=="C" and h>3 and 1971<=a<=1981:
    print("APROBADO")
elif i>2500000 and e=="S" and v=="U":
    print("APROBADO")
elif i>3500000 and a>5:
    print("APROBADO")
elif v=="R" and e=="C" and h<2:
    print("APROBADO")
else:
    print("RECHAZADO")  