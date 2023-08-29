#Aprobación de créditos
dinero = eval(input("Ingrese plata"))
año_nacimiento = eval(input("Ingrese año de nacimiento"))
hijos = eval(input("Ingrese cantidad de hijos"))
antiguedad = eval(input("Ingrese años de antiguedad"))
estado_civil = input("Ingrese estado civil")
habitat = input("Ingrese si vive en ciudad o campo")

año = 2020 - año_nacimiento

if(antiguedad <= 10 and hijos <= 2):
  print("APROBADO")
elif(estado_civil == "C" and hijos <= 4 and año_nacimiento > 1965 and año_nacimiento < 1975):
  print("APROBADO")
elif(dinero <= 2500000 and estado_civil == "S" and habitat):
  print("APROBADO")
elif(dinero <= 3500000 and antiguedad <= 5):
  print("APROBADO")
elif(habitat and estado_civil == "C" and hijos >= 2):
  print("APROBADO")
else:
  print("RECHAZO")      