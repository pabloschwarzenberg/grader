i = int(input("Ingreso mensual en pesos: "))
a = int(input("Año de nacimiento: "))
h = int(input("Numero de hijos: "))
p = int(input("Años de permanecia al banco: "))
e = input("Estado civil (S: soltero, C: casado): ")
v = input("Si vive en campo o cuidad (U: urbano, R: rural)")

if(p > 10 and h >= 2):
  print("APROBADO")

elif((e == "C" or e == "c") and h >= 3 and a >= 1968 and a <= 1978):
  print("APROBADO")

elif(i > 2500000 and (e == "s" or e == "S") and (v == "U" or v == "u")):
  print("APROBADO")

elif(i > 3500000 and p > 5):
  print("APROBADO")
  
elif((v == "r" or v == "R") and (e == "c" or e == "C") and h < 2):
  print("APROBADO")

else:
  print("RECHAZADO")