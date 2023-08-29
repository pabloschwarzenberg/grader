#Aprobación de créditos
ingreso=float(input("Entregue el monto de su ingreso (En pesos): "))
nacimiento=int(input("Ingrese su fecha de nacimiento: "))
edad=(2022-nacimiento)
hijos=input("Ingrese el numero de hijos: ")
banco=input("¿Cuantos años de pertenecencia tiene en el banco: ")
civil=input("¿Cual es su estado civil? (S: soltero, C: casado): ")
casa=input("¿Vive en campo o ciudad? (U: ciudad, R: campo): ")

if int(banco>=10 and hijos>=2):
    print("APROBADO")
if int(civil == "C" and hijos > 3 and edad>45 and edad<55):
    print("APROBADO")
if int(ingreso>2500000 and civil=="S" and casa=="U"):
    print("APROBADO")
if int(ingreso>3500000 and banco>5):
    print("APROBADO")
if int(casa=="R" and civil=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")