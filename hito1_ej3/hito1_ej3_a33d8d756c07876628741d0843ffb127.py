ingreso= eval(input("indique su ingreso (en pesos): $"))
nacimiento= eval(input("indique su año de nacimiento: "))
hijos= eval(input("indique el número de hijos: "))
pertenencia= eval(input("indique la cantidad de años de pertenencia al banco: "))
estado= input("indique su estado civil (S=soltero o C=casado): ")
vivienda= input("indique si vive en campo o ciudad (u=urbano o r=rural): ")
#El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:
if(pertenencia>10 and hijos>=2):
  print("APROBADO")
elif(estado.upper()=="C" and hijos>3 and 1975>nacimiento>1965):
  print("APROBADO")
elif(ingreso>2500000 and estado.upper()=="S" and vivienda.upper()=="U"):
  print("APROBADO")
elif(ingreso>3500000 and pertenencia>5):
  print("APROBADO")
elif(vivienda.upper()=="R" and estado.upper()=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")