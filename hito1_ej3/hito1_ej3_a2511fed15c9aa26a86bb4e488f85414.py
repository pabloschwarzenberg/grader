#ingreso
I = int(input("ingrese su Ingreso (en pesos): "))      
#año de nacimiento
AN = int(input("ingrese su año de nacimiento: "))
AN = 2021 - AN
#numero de hijos
NH = int(input("ingrese su numero de hijos: "))
#años de pertenencia al banco
AP = int(input("ingrese cuantos años a pertenecido al banco: "))
#estado civil
EC = str(input("ingrese su estado civil (S: soltero, C, casado): "))
#donde vive
DV = str(input("ingrese donde vive (U: urbano, R: rural): "))

if AP > 10 and NH >= 2:
  print("APROBADO")

elif EC == "C" and 45 <= AN <= 55 and NH > 3:
  print("APROBADO")

elif I > 2500000 and EC == "S" and DV == "U":
  print("APROBADO")

elif I > 3500000 and AP > 5: 
  print("APROBADO")

elif DV == "R" and EC == "C" and NH < 2:
  print("APROBADO")

else:
  print("RECHAZADO")


