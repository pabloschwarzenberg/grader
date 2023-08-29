#Aprobación de créditos
In = float(input("Ingreso (en pesos): "))   
A = int(input("Año de nacimiento: "))  
N = int(input("Numero de hijos: "))  
AP = int(input("Años de pertenencia al banco: "))  
EC = str(input('"S": Soltero, "C": Casado: '))
L = str(input('Si vive en campo o ciudad: "U": Urbano, "R": Rural: '))
if AP > 10 :
 if N >= 2 :
  print ("APROBADO")
if EC == "C" :
 if N > 3 :
  if  45 < 2017 - A < 55 :
   print ("APROBADO")
if In > 2500000 :
 if EC == "S" :
  if L == "U" :
   print ("APROBADO")
if In > 3500000 :
 if AP > 5 :
  print ("APROBADO")
if L == "R" :
 if EC == "C" :
  if N < 2 :
   print ("APROBADO")
else :
 print ("RECHAZADO")