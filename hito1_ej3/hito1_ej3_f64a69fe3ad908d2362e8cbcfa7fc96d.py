ing = int (input("Ingreso en pesos: "))
anc = int (input("Año de nacimiento: "))
numh= int (input("Número de hijos:"))
apb = int(input("Años de pertenencia en el banco:"))
esc = input("Estado civil ( S: soltero y C: casado)")
viv= input("Vive en campo o cuidad (U: urbano, R: rural)")
anc2= 2022-anc
if ing >= 2500000 or esc == "S" or viv == "R":
  print ("APROBADO")
elif ing >= 3500000 and apb > 5:
  print ("APROBADO")
elif apb > 10 and numh >= 2:
  print ("APROBADO")
elif esc == "C" and numh > 3 and anc2 >= 45 and anc2 <=55: 
  print ("APROBADO")
elif viv == "U" and esc == "C" and numh < 2:
  print ("APROBADO")
else:
  print ("RECHAZADO")