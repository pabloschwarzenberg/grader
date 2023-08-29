ingreso = int (input ("ingrese sus ingresos en pesos: "))
nacimiento= int (input ("ingrese su año de nacimiento: "))
nhijos = int (input ("ingrese cantidad de hijos: "))
abanco = int (input ("ingrese años de pertenencia en banco: "))
ecivil = input ("Ingrese estado civil: S para soltero y C para casado: ")
vive = input ("Ingrese si vive en el Campo como R o ciudad como U:")

while not (ecivil == "C" or ecivil =="S"):
   ecivil = input ("Error. Ingrese estado civil: S para soltero y C para casado: ")
while not (vive == "R" or vive =="U"):
   vive = input ("Error, Ingrese si vive en el Campo como R o ciudad como U:")

edad = 2020 - nacimiento
if abanco >=10 and nhijos >=2:
    print ("APROBADO")
elif ecivil == "C" and nhijos >= 3 and edad >=45 and edad <=55:
    print ("APROBADO")
elif ingreso >=2500000 and ecivil == "S" and vive == "U":
    print ("APROBADO")
elif ingreso >=3500000 and abanco >=5:
    print ("APROBADO")
elif vive == "R" and ecivil == "C" and nhijos <=2:
    print ("APROBADO")
else:
    print ("RECHAZADO")
