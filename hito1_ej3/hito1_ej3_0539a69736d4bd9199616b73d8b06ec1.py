#Aprobación de créditos
a = int(input("Ingresos: "))
b = int(input("Año de nacimiento: "))
c = int(input("Numero de hijos: "))
d = int(input("Años de pertenencia al banco: "))
e = str(input("Estado civil (S: soltero, C: casado): "))
f = str(input("en donde vive campo(R) o ciudad(U): "))
g = (b - 2021)

if (d > 10 and c >=2):
    print ("APROBADO")
elif (e == "C" or e == "c" and c > 3 and g >= 45 and g <=55):
    print ("APROBADO")
elif (a > 2500000 and e == "S" or e == "s" and f == "U" or f == "u"):
    print ("APROBADO")
elif (a > 3500000 and d > 5):
    print ("APROBADO")
elif (f == "R" or f == "r" and e == "C" or e == "c" and c < 2):
    print ("APROBADO")
else:
    print ("RECHAZADO")
