#Aprobación de créditos
print("Rellene los siguientes datos")
a=int(input("Ingreso(en pesos):"))
b=int(input("Año de nacimiento:"))
c=int(input("Número de hijos:"))
d=int(input("Años de pertenencia al banco:"))
e=input("Estado civil (S: soltero, C: casado):")
f=input("Si vive en campo o cuidad (U: urbano, R: rural):")
g=2017-b
if(d>10 and c>=2):
    print("APROBADO")
elif(e=="C" and c>3 and 55>=g>=45):
    print("APROBADO")
elif(a>2500000 and e=="S" and f=="U"):
    print("APROBADO")
elif(a>3500000 and d>5):
    print("APROBADO")
elif(f=="R" and e=="C" and 2>c):
    print("APROBADO")
else:
    print("REPROBADO")  