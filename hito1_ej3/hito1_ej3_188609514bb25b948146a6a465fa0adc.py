#Aprobación de créditos
a = int(input("ingreso en pesos: "))
b = int(input("ingrese año de nacimiento: "))
c = int(input("ingrese numero de hijos: "))
d = int(input("ingrese años de pertenencia al banco: "))
e = str(input("ingrese su estado civil (S: soltero, C: casado:): "))
f = str(input("ingrese si vive en campo o cuidad (U: urbano, R: rural): "))


if (d>10 and c>=2):
    print("APROBADO")
    
elif (e=="C" and c>3 and 45<=(2017-b)<=55):
    print("APROBADO")
    
elif (a>2500000 and e=="S" and f=="R"):
    print("APROBADO")

elif (a>3500000 and d>5):
    print("APROBADO")

elif (f=="R" and e=="C" and c<2):
    print("APROBADO")

else :
    print("RECHAZADO")
