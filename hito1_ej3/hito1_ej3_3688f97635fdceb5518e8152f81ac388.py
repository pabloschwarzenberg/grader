#Aprobación de créditos
I = eval(input("ingreso en pesos:"))
AN = eval(input("año de nacimiento:"))
E = eval(input("edad:"))
NJ = eval(input("numero de hijos:"))
BP = eval(input("año de pertenencia del banco:"))
estado = input("Estado civil (S: soltero, C:, casado)")
vive = input("vivienda en (U: urbano, R: rural)")

#reglas para la aprovacion del credito , con una de ellas que se cumpla, se aprueba el credito
if BP > 10 and NJ >= 2:
   print("aprobado")
elif estado == "C" and NJ >= 3 and AN >= 1975 and AN <= 1965:
   print("aprobado")
elif I > 2500000 and estado == "S" and vive == "U":
   print("aprobado")
elif I > 3500000 and BP > 5:
   print("aprobado")
elif vive == "R" and estado == "C" and NJ < 2:
   print("aprobado")
else:
  print("rechazado")