#Aprobación de créditos

ING = int(input("Ingreso: "))
NAC = int(input("Anio de nacimiento: "))
HIJ = int(input("Numero de hijos: "))
PER = int(input("Anios de permanencia en el banco: "))
EST = input("Estado civil (S: [S]oltero  ;  C: [C]asado): ")
ZON = input("Zona (R: [R]ural  ;  U: [Urbana]): ")



if (PER >= 10) and (HIJ >= 2):
	out = "APROBADO"
	
elif (EST == "C") and (HIJ > 3) and ( (2021 - NAC)>=45 and  (2021 - NAC) <= 55):
	out = "APROBADO"

elif (ING >= 2500000) and (EST == "S") and (ZON == "U"):
	out = "APROBADO"

elif (ING >= 3500000) and (PER >= 5):
	out = "APROBADO"
	
elif (ZON == "R") and (EST == "C") and (HIJ < 2):
	out = "APROBADO"
	
else:
	out = "RECHAZADO"
  
  
print(out)