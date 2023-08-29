#Aprobación de créditos
ingreso=int(input("ingrese su ingreso en pesos: "))
year=int(input("ingrese su año de nacimiento: "))
hijos=int(input("ingrese la cantidad de hijos que posee: "))
banco=int(input("ingrese la cantidad de años a la que a pertenecido al banco: "))
estado=str(input("ingrese su estado civil(S=Soltero - C=Casado): "))
vive=str(input("Ingrese si vive en campo o ciudad(U=Urbano - R=Rural): "))
if(banco>10 and hijos>=2):
    print("APROBADO")

elif(estado=="C" and hijos>3 and year>=45 and year<=55):
    print("APROBADO")

elif(ingreso>2500000 and estado=="S" and vive=="U"):
    print("APROBADO")

elif(ingreso>3500000 and banco>5):
    print("APROBADO")

elif(vive=="R" and estado=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")