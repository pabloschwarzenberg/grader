#Aprobación de créditos
print("ingrese la información solicitada")
ingreso=int(input("ingreso en pesos: "))
nac=int(input("año de nacimiento: "))
hijos=int(input("número de hijos: "))
tiempo=int(input("años de pertenencia al banco: "))
estado=input("estado civil, 'S'=soltero, 'C'=casado: ")
ubicacion=input("ubicación , 'U'=urbano, 'R'=rural: ")
resultado=""
if(tiempo>10 and hijos>=2):
    resultado="APROBADO"
elif(estado=="C" and hijos>3 and nac>=1975 and nac<=1975):
    resultado="APROBADO"
elif(ingreso>2500000 and estado=="S" and ubicacion=="U"):
    resultado="APROBADO"
elif(ingreso>3500000 and tiempo>5):
    resultado="APROBADO"
elif(ubicacion=="R" and estado=="C" and hijos<2):
    resultado="APROBADO"
else:
    resultado="RECHAZADO"
print(resultado)