#Aprobación de créditos
print("ingrese los datos del postulante")
i=(int(input("cual es su ingreso?")))
a=(int(input("cual es su año de nacimiento?")))
h=(int(input("cual es la cantidad de hijos que tiene?")))
p=(int(input("cuales son sus años de pertenencia al banco?")))
e=(str(input("cual es su estado civil? escriba una S para soltero y C para casado")))
z=(str(input("cual es el sector en donde vive? escriba una U para urbano y R para rural")))
ed=2022-a
if p>10 and h>=2:
    print("APROBADO")
elif z=="C" and h>3 and ed>45 and ed<55:
    print("APROBADO")
elif i>2500000 and e=="S" and z=="U":
    print("APROBADO")
elif i>3500000 and p>5:
    print("APROBADO")
elif z=="R" and e=="C" and h<2:
    print("APROBADO")
else:
    print("RECHAZADO")      