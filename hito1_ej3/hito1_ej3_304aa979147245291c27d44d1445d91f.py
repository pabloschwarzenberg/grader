#Aprobación de créditos
print("\nAprobacion de creditos\n")

ingreso=int(input("Introduzca su ingreso en pesos: "))
nacimiento= int(input("Indique su año de nacimiento: "))
hijos=int(input("Introduzca la cantidad de hijos que tiene: "))
pertenencia= int(input("Indique los años de pertenencia al banco: "))
estado= input("Indique su estado civil (S: soltero, C, casado)")
vivienda=input("Indique donde vive (U: urbano, R: rural)")

edad= int(2022-nacimiento)

if (pertenencia>10 and hijos>=2):
    print ("APROBADO")
elif (estado=="C" and hijos>3 and edad>45 and edad<55 ):
    print ("APROBADO")
elif (ingreso >2500000 and estado == "C" and vivienda =="U"):
    print ("APROBADO")
elif(ingreso >3500000 and pertenencia>5):
    print ("APROBADO")
elif(vivienda=="R" and estado=="C" and hijos<2):
    print ("APROBADO")
else:
    print ("RECHAZADO")      