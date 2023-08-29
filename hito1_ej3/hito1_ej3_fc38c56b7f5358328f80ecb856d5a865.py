#Aprobación de créditos
ingreso=int(input("cuanto es su ingreso en pesos: "))
ano=int(input("año de nacimiento: "))
hijos=int(input("numero de hijos: "))
banco=int(input("años de pertenencia al banco: "))
civil=str(input("ingrese estado civil(S: soltero o C: casado): "))
vive=str(input("vive en campo o ciudad(U: urbano o R: rural): "))
edad=2017-ano

if banco >= 10 and hijos >=2:
    print("APROBADO")
elif civil=="C" and hijos >=3 and 45 <= edad <= 55:
    print("APROBADO")
elif ingreso > 3500000 and banco > 5:
    print("APROBADO")
elif vive =="R" and hijos <2:
    print("APROBADO")
else:
    print("RECHAZADO")      